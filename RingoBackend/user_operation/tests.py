from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from goods.models import Goods, GoodsCategory
from django.contrib.auth.models import User
from login.serializer import UserSerializer
from django.urls import reverse
from django.test import Client
from django.forms.models import model_to_dict
import datetime
import json



# Create your tests here.
class UserNeedTest(TestCase):

   def test_list(self):
      user1 = User.objects.create_user(username = 'user1', password = '123', email='user1@user1.com')
      user2 = User.objects.create_user(username = 'user2', password = '123', email='user1@user1.com')
      category = GoodsCategory.objects.create(name="category", category_type = 1)
 
      need1 = Goods.objects.create(property_type=0,category=category,emergency=5,user=user1,name='need1',address='addr',goods_brief="need1")
      need2 = Goods.objects.create(property_type=0,category=category,emergency=3,user=user2,name='need2',address='addr',goods_brief="need2")
   
      send_data ={'username':'user1', 'password':'123'}
      res = self.client.post('/apis/login/login', data = send_data)
      res_data = res.json()
      token = res_data.get('token')

      headers = {'Authentication': 'Token  ' + token}
      res = self.client.get('/apis/need/', HTTP_AUTHORIZATION = 'JWT  ' + token)
      res_data = res.json()
      for good in res_data.get('results'):
         self.assertNotEqual(good.get('name'),need2)

   def test_update(self):
      user1 = User.objects.create_user(username = 'user1', password = '123', email='user1@user1.com')
      category = GoodsCategory.objects.create(name="category", category_type = 1, code=1, desc='sds')
 
      need1 = Goods.objects.create(property_type=0,category=category,emergency=5,user=user1,name='need1',address='addr',goods_brief="need1")

   
      send_data ={'username':'user1', 'password':'123'}
      res = self.client.post('/apis/login/login', data = send_data)
      res_data = res.json()
      token = res_data.get('token')
      need1 = Goods.objects.get(name='need1')
      good_sn = need1.goods_sn
      data_need1 = model_to_dict(need1)
      category1 = model_to_dict(category)
      
      data_need1['name'] = 'needneed1'
      data_need1['goods_desc'] = 'needneed1'
      data_need1['category'] = category1
      res = self.client.put(f'/apis/need/{good_sn}/', HTTP_AUTHORIZATION = 'JWT  ' + token, data=data_need1, content_type ='application/json')
      res = self.client.get('/apis/need/', HTTP_AUTHORIZATION = 'JWT  ' + token)
      need1 = Goods.objects.get(goods_sn=good_sn)
      self.assertEqual(need1.name, 'needneed1')

   def test_create(self):
      user1 = User.objects.create_user(username = 'user1', password = '123', email='user1@user1.com')
      category = GoodsCategory.objects.create(name="category", category_type = 1, code=1, desc='sds')
 
   
      send_data ={'username':'user1', 'password':'123'}
      res = self.client.post('/apis/login/login', data = send_data)
      res_data = res.json()
      token = res_data.get('token')
      category1 = model_to_dict(category)


      data_need1 = {}
      data_need1["property_type"] = 0
      data_need1["name"] = 'need5'
      data_need1['category'] = category1
      res = self.client.post(f'/apis/need/', HTTP_AUTHORIZATION = 'JWT  ' + token, data=data_need1, content_type ='application/json')
      res_data = res.json()
      self.assertEqual(res_data['name'], data_need1['name'])



class UserOfferingTest(TestCase):
   
   def test_list(self):
      user1 = User.objects.create_user(username = 'user1', password = '123', email='user1@user1.com')
      user2 = User.objects.create_user(username = 'user2', password = '123', email='user1@user1.com')
      category = GoodsCategory.objects.create(name="category", category_type = 1)
 
      need1 = Goods.objects.create(property_type=1,category=category,emergency=5,user=user1,name='need1',address='addr',goods_brief="need1")
      need2 = Goods.objects.create(property_type=1,category=category,emergency=3,user=user2,name='need2',address='addr',goods_brief="need2")
   
      send_data ={'username':'user1', 'password':'123'}
      res = self.client.post('/apis/login/login', data = send_data)
      res_data = res.json()
      token = res_data.get('token')

      headers = {'Authentication': 'Token  ' + token}
      res = self.client.get('/apis/offering/', HTTP_AUTHORIZATION = 'JWT  ' + token)
      res_data = res.json()
      for good in res_data.get('results'):
         self.assertNotEqual(good.get('name'),need1)

   def test_update(self):
      user1 = User.objects.create_user(username = 'user1', password = '123', email='user1@user1.com')
      category = GoodsCategory.objects.create(name="category", category_type = 1, code=1, desc='sds')
 
      need1 = Goods.objects.create(property_type=1,category=category,emergency=5,user=user1,name='need1',address='addr',goods_brief="need1")

   
      send_data ={'username':'user1', 'password':'123'}
      res = self.client.post('/apis/login/login', data = send_data)
      res_data = res.json()
      token = res_data.get('token')
      need1 = Goods.objects.get(name='need1')
      good_sn = need1.goods_sn
      data_need1 = model_to_dict(need1)
      category1 = model_to_dict(category)
      
      data_need1['name'] = 'needneed1'
      data_need1['goods_desc'] = 'needneed1'
      data_need1['category'] = category1
      res = self.client.put(f'/apis/offering/{good_sn}/', HTTP_AUTHORIZATION = 'JWT  ' + token, data=data_need1, content_type ='application/json')
      res = self.client.get('/apis/offering/', HTTP_AUTHORIZATION = 'JWT  ' + token)
      need1 = Goods.objects.get(goods_sn=good_sn)
      self.assertEqual(need1.name, 'needneed1')

   def test_create(self):
      user1 = User.objects.create_user(username = 'user1', password = '123', email='user1@user1.com')
      category = GoodsCategory.objects.create(name="category", category_type = 1, code=1, desc='sds')
 
   
      send_data ={'username':'user1', 'password':'123'}
      res = self.client.post('/apis/login/login', data = send_data)
      res_data = res.json()
      token = res_data.get('token')
      category1 = model_to_dict(category)


      data_need1 = {}
      data_need1["property_type"] = 1
      data_need1["name"] = 'need5'
      data_need1['category'] = category1
      res = self.client.post(f'/apis/offering/', HTTP_AUTHORIZATION = 'JWT  ' + token, data=data_need1, content_type ='application/json')
      res_data = res.json()
      self.assertEqual(res_data['name'], data_need1['name'])



class PersonalProfileTest(TestCase):
   def setUp(self) -> None:
      super().setUp()
      self.user1 = User.objects.create_user(username='测试用户1', email='cs1@111.com', password='88888888')
      self.user2= User.objects.create_user(username='测试用户2', email='cs2@111.com', password='88888888')
      self.user1.save()
      self.user2.save()
      self.jwt1 = 'JWT  ' + self.client.post(reverse('login'), {'username':'测试用户1', 'password':'88888888'}).data['token']
      self.jwt2 = 'JWT  ' + self.client.post(reverse('login'), {'username':'测试用户2', 'password':'88888888'}).data['token']
   
   def test_initialize_by_get(self):
      resp = self.client.get(reverse('personal_profile'), HTTP_AUTHORIZATION = self.jwt1)
      self.assertEqual(resp.status_code, 200)
      self.assertEqual(resp.data['nickname'], '请输入昵称')
      self.assertEqual(resp.data['address'], "请输入地址")
   
   def test_initialize_by_post(self):
      resp = self.client.post(reverse('personal_profile'), HTTP_AUTHORIZATION = self.jwt1, data = {})
      self.assertEqual(resp.status_code, 200)

   def test_update_1(self):
      resp = self.client.post(reverse('personal_profile'), HTTP_AUTHORIZATION = self.jwt1, data = {'nickname':'狗子'})
      self.assertEqual(resp.status_code, 200)
      self.assertEqual(resp.data['nickname'], '狗子')
   
   def test_update_2(self):
      resp = self.client.post(reverse('personal_profile'), HTTP_AUTHORIZATION = self.jwt2, data = {'nickname':'狗子', 'address':'德国 不莱梅', 'signature':'お姉ちゃん達は気を付けて。次はわたしの番よ。'})
      self.assertEqual(resp.status_code, 200)
      self.assertEqual(resp.data['nickname'], '狗子')
      self.assertEqual(resp.data['address'], '德国 不莱梅')
      self.assertEqual(resp.data['signature'], 'お姉ちゃん達は気を付けて。次はわたしの番よ。')