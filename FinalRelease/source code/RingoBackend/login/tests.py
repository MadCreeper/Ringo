from django.test import TestCase
from login.constants import *
from login.models import User
from django.urls import reverse
import login.views as lview
import logging



# Create your tests here.
# class SmokeTestCase(TestCase):
#     def test_smoke(self):
#         self.assertEqual(1+1, 2)

class LoginTest(TestCase):
    # 针对登录功能的测试
    # 由于登录功能是调用标准库函数代码，不需要测试
    pass

class RegisterTest(TestCase):
    '''
    - 针对注册功能的测试
    - 除了发送邮件的功能无法完成自动化测试之外，其它内容都进行测试
    - 由于空串问题已在前端得到解决，所以此处不进行测试
    '''
    def setUp(self) -> None:
        testUser = User.objects.create_user(username='测试用户1',email='test@test.com', password='password')
        testUser.save()
        super().setUp()

    # 测试输入重复名称
    def test_username_exists(self):
        data = {'username': '测试用户1'}
        response = self.client.post(reverse('register'), data=data)
        self.assertEqual(response.data[ERROR_CODE], ERR_REG_USERNAME_EXIST)
    
    def test_invalid_email(self):
        data = {'username':'Roland', 'email': 'hahahahaha'}
        response = self.client.post(reverse('register'), data=data)
        self.assertEqual(response.data[ERROR_CODE], ERR_INVALID_EMAIL)

    # 测试输入重复邮箱
    def test_email_exists(self):
        data = {'username':'Roland', 'email': 'test@test.com'}
        response = self.client.post(reverse('register'), data=data)
        self.assertEqual(response.data[ERROR_CODE], ERR_REG_EMAIL_EXIST)

    # 测试输入错误的验证码 以及 光速QA被拒绝 （验证码直接从后端读取，而不经过邮箱）
    def test_wrong_vericode(self):
        data = {'username':'Roland', 'email': 'black_silencer@test.com'}
        response = self.client.post(reverse('register'), data=data)
        veriCodeDict = lview.get_curr_dict()
        veriCode = veriCodeDict.get('black_silencer@test.com')[1]
        self.assertEqual(response.data[ERROR_CODE], MAIL_SEND_SUCCESS)
        # 快速请求
        response = self.client.post(reverse('register'), data=data)
        self.assertEqual(response.data[ERROR_CODE], ERR_REG_VERIFICATION_REQUEST_TOO_FREQUENT)

        data['veriCode'] = veriCode + '114514'
        response = self.client.post(reverse('register'), data=data)
        self.assertEqual(response.data[ERROR_CODE], ERR_REG_WRONG_VERIFICATION)

    # 测试正常流程一波全通
    def test_normal(self):
        data = {'username':'Roland', 'email': 'black_silencer@test.com', 'password':'angela'}
        response = self.client.post(reverse('register'), data=data)
        veriCodeDict = lview.get_curr_dict()
        veriCode = veriCodeDict.get('black_silencer@test.com')[1]
        self.assertEqual(response.data[ERROR_CODE], MAIL_SEND_SUCCESS)
        data['veriCode'] = veriCode
        response = self.client.post(reverse('register'), data=data)
        self.assertEqual(response.data[ERROR_CODE], NO_ERR)

        responseLogin = self.client.post(reverse('login'), data=data)
        self.assertEqual(responseLogin.status_code, 200)



class PasswordChangeTest(TestCase):
    ''' 测试密码修改 '''
    # 于初始化中获取jwt token
    def setUp(self):
        super().setUp()
        user = User.objects.create_user(username='hod', email='abba@aadd.com', password='hodspassword')
        user.save()
        data = {'username':'hod', 'password':'hodspassword'}
        resp = self.client.post(reverse('login'), data=data)
        self.jwt_code = "JWT  " + resp.data.get('token')
        logging.debug(self.jwt_code)

    # 测试用户输入的原始密码错误
    def test_wrong_pwd(self):
        data = {'password':'wrongpassword'}
        resp = self.client.post(reverse('reset_password'), HTTP_AUTHORIZATION = self.jwt_code, data=data)
        self.assertEqual(resp.data[ERROR_CODE], ERR_PWDCHANGE_WRONGPWD)

    # 测试用户输入完全正确
    def test_correct_pwd(self):
        data = {'password':'hodspassword', 'newPassword1':'hodsnewpassword', 'newPassword1':'hodsnewpassword'}
        resp = self.client.post(reverse('reset_password'), HTTP_AUTHORIZATION = self.jwt_code, data=data)
        self.assertEqual(resp.data[ERROR_CODE], NO_ERR)
        
        data = {'password':'hodsnewpassword', 'newPassword1':'hodspassword1', 'newPassword2':'hodspassword1'}
        resp = self.client.post(reverse('reset_password'), HTTP_AUTHORIZATION = self.jwt_code, data=data)
        self.assertEqual(resp.data[ERROR_CODE], NO_ERR)

        data = {'password':'hodspassword1', 'newPassword1':'hodspassword', 'newPassword2':'hodspassword'}
        resp = self.client.post(reverse('reset_password'), HTTP_AUTHORIZATION = self.jwt_code, data=data)
        self.assertEqual(resp.data[ERROR_CODE], NO_ERR)

    # 测试用户输入了空串（不必要的，但是代码里有这一部分，就进行了测试）
    def test_empty_data(self):
        data = {'password':'hodspassword', 'newPassword1':'', 'newPassword1':''}
        resp = self.client.post(reverse('reset_password'), HTTP_AUTHORIZATION = self.jwt_code, data=data)
        self.assertEqual(resp.data[ERROR_CODE], EMPTY_DATA)
        data =  {'password':'hodspassword'}
        resp = self.client.post(reverse('reset_password'), HTTP_AUTHORIZATION = self.jwt_code, data=data)
        self.assertEqual(resp.data[ERROR_CODE], EMPTY_DATA)
    
class PasswordForgetTest(TestCase):
    '''
    测试在不进行登录（忘记密码）时通过邮箱找回
    类似地，邮件发送部分将不进行自动化测试。
    '''
    def setUp(self) -> None:
        super().setUp()
        testUser = User.objects.create_user(username='testguy1', password='88888888', email='1145@514yj.com')
        testUser.save()
    
    def test_invalid_email(self):
        data = {'email':'invalidemail'}
        resp = self.client.post(reverse('forget_password'), data=data)
        self.assertEqual(resp.data[ERROR_CODE], ERR_INVALID_EMAIL)
    
    def test_email_not_exists(self):
        data = {'email':'notexist@404notfound.com'}
        resp = self.client.post(reverse('forget_password'), data=data)
        self.assertEqual(resp.data[ERROR_CODE], ERR_PWDCHANGE_EMAIL_NOTEXIST)

    def test_mail_send(self):
        data = {'email':'1145@514yj.com'}
        
        resp = self.client.post(reverse('forget_password'), data=data)
        self.assertEqual(resp.data[ERROR_CODE], MAIL_SEND_SUCCESS)
        
        resp = self.client.post(reverse('forget_password'), data=data)
        self.assertEqual(resp.data[ERROR_CODE], ERR_PWDCHANGE_VERIFY_TOO_FREQUENT)

        veriDict = lview.get_curr_dict()
        veriCode = veriDict[data['email']][1]

        wrongVeriCode = veriCode + 'wrong'
        data['veriCode'] = wrongVeriCode
        data['password'] = '114514'
        resp = self.client.post(reverse('forget_password'), data=data)
        self.assertEqual(resp.data[ERROR_CODE], ERR_PWDCHANGE_VERIFY_FAIL)

        data['veriCode'] = veriCode
        resp = self.client.post(reverse('forget_password'), data=data)
        self.assertEqual(resp.data[ERROR_CODE], NO_ERR)





