from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from login.models import User
from login.serializer import UserSerializer, HelperSerializer
from login.helpers import codeGenerator, mailSend, emailChecker
import datetime
from django.contrib.auth.hashers import make_password
from rest_framework import permissions
from rest_framework_jwt.authentication import jwt_decode_handler
from django.contrib.auth import authenticate

from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from login.constants import *

# Create your views here.
# Constants



# stores 
veriCodeHash= {}

class UserRegisterView(APIView):
    # 测试用代码：
    queryset = User.objects.all()
    # serializer_class = UserSerializer
    serializer_class = HelperSerializer
    ###
    def post(self, request, format = None):
        dataDict = {
            'username' : request.data.get('username'),
            'email' : request.data.get('email'),
            'password' : request.data.get('password'),
            'veriCode' : request.data.get('veriCode')
        }
        username = dataDict.get('username')
        email = dataDict.get('email')
        if User.objects.filter(username = username):
            # 用户名已存在
            return Response(data={ERROR_CODE: ERR_REG_USERNAME_EXIST, **dataDict})
        elif not emailChecker.check_mail_regex(email):
            return Response(data={ERROR_CODE: ERR_INVALID_EMAIL, **dataDict})
        elif User.objects.filter(email = email):
            # 邮箱已被注册
            return Response(data = {ERROR_CODE: ERR_REG_EMAIL_EXIST, **dataDict})
        elif not dataDict.get('veriCode'):
            # 未填写验证码信息， 发送验证码
            if veriCodeHash.get(email):
                # 查看验证码是否已经被发送过
                timestamp = veriCodeHash.get(email)[0]
                now = datetime.datetime.now().timestamp()
                delta = now - timestamp
                if delta < 60:
                    # 申请验证码间隔时间过短，不允许
                    return Response(data={ERROR_CODE: ERR_REG_VERIFICATION_REQUEST_TOO_FREQUENT, **dataDict})
            veriCode = codeGenerator.generateCode()
            veriCodeHash[email] = (datetime.datetime.now().timestamp(), veriCode)
            mailSend.sendMail(receiver=email, validation=veriCode,username=username)
            return Response(data = {ERROR_CODE: MAIL_SEND_SUCCESS, **dataDict})
        else:
            veriCode = dataDict.get('veriCode')
            veriCodeStored = veriCodeHash.get(email)
            if not veriCodeStored or veriCodeStored[1] != veriCode:
                # 验证码验证不通过
                return Response({ERROR_CODE: ERR_REG_WRONG_VERIFICATION, **dataDict})
            veriCodeHash.pop(email)
            mData = {
                'username' : request.data.get('username'),
                'password' : make_password(request.data.get('password')),
                'email' : request.data.get('email')
            }
            serializer = UserSerializer(data=mData)
            if serializer.is_valid():
                serializer.save()
                return Response(data = {ERROR_CODE:NO_ERR, **serializer.data}, status = status.HTTP_201_CREATED)
            return Response()



class UserPasswordChangeView(APIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def post(self, request, format = None):
        curr_user = request.user
        # serializer = UserSerializer(curr_user)
        data = {
            'password':request.data.get('password'),
            'newPassword1':request.data.get('newPassword1'),
            'newPassword2':request.data.get('newPassword2')
        }
        if authenticate(username = curr_user.username, password = data.get('password')) is not None:
            if data.get('newPassword1'):
                curr_user.set_password(data.get('newPassword1'))
                curr_user.save()
                return Response(data = {ERROR_CODE:NO_ERR,})
            else:
                return Response(data = {ERROR_CODE: EMPTY_DATA})
        else:
            return Response(data = {ERROR_CODE: ERR_PWDCHANGE_WRONGPWD})
        



class UserPasswordForgottenView(APIView):
    # 测试用代码
    serializer_class = HelperSerializer

    def post(self, request, format = None):
        dataDict = {
            'email': request.data.get('email'),
            'veriCode': request.data.get('veriCode'),
            'password': request.data.get('password')
        }

        email = dataDict.get('email')
        veriCode = dataDict.get('veriCode')
        password = dataDict.get('password')
        if not emailChecker.check_mail_regex(email):
            return Response(data={ERROR_CODE: ERR_INVALID_EMAIL, **dataDict})
        elif not User.objects.filter(email = email):
            return Response({ERROR_CODE:ERR_PWDCHANGE_EMAIL_NOTEXIST, **dataDict})
        elif not veriCode:
            # 进入发码逻辑
            if veriCodeHash.get(email):
                # 查看验证码是否已经被发送过
                timestamp = veriCodeHash.get(email)[0]
                now = datetime.datetime.now().timestamp()
                delta = now - timestamp
                if delta < 60:
                    # 申请验证码时间过短，不允许
                    return Response(data={ERROR_CODE:ERR_PWDCHANGE_VERIFY_TOO_FREQUENT, **dataDict})
            veriCode = codeGenerator.generateCode()
            veriCodeHash[email] = (datetime.datetime.now().timestamp(), veriCode)
            curr_user = User.objects.get(email = email)
            mailSend.sendMail(receiver=email, validation=veriCode, username = curr_user.username)
            return Response(data = {ERROR_CODE:MAIL_SEND_SUCCESS, **dataDict})
        else:
            veriCodeStored = veriCodeHash.get(email)
            if not veriCodeStored or veriCodeStored[1] != veriCode:
                # 验证码验证不通过
                return Response({ERROR_CODE: ERR_PWDCHANGE_VERIFY_FAIL, **dataDict})
            veriCodeHash.pop(email)
            curr_user = User.objects.get(email = email)
            curr_user.set_password(password)
            curr_user.save()
            serializer = UserSerializer(curr_user)
            return Response(data = {ERROR_CODE:NO_ERR, **serializer.data})



class CustomAuthenticationBackend(ModelBackend):
    def authenticate(self, request, username, password, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(email = username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None
        return None

def get_curr_dict():
    return veriCodeHash.copy()