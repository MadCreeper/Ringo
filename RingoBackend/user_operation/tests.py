from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from goods.models import Goods, GoodsCategory
from django.contrib.auth.models import User
from login.serializer import UserSerializer
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
# class UserOfferingTest(TestCase):
#     """测试物品类模型"""


#     def test_category_model(self):
#         """测试物品种类"""
#         topCategory = GoodsCategory.objects.create(name="topcategory", category_type = 1)

#         secondCategory = GoodsCategory.objects.create(name="secondcategory", category_type = 2, parent_category=topCategory)

#         thirdCategory = GoodsCategory.objects.create(name="thirdcategory", category_type = 3, parent_category=secondCategory)

#       #----------测试是否成功创建---------------
#         self.assertTrue(topCategory is not None)
#         self.assertTrue(secondCategory is not None)
#         self.assertTrue(thirdCategory is not None)
#       #----------测试父类关系是否正常------------------
#         self.assertEqual(topCategory.parent_category, None)
#         self.assertEqual(secondCategory.parent_category, topCategory)
#         self.assertEqual(thirdCategory.parent_category, secondCategory)
#       #---------------测试缺省值是否为空----------------
#         self.assertEqual(thirdCategory.desc, '')
#         self.assertEqual(thirdCategory.code, '')


#     def test_good_model(self):
#         """测试物品表"""
#         user = User.objects.create(username = 'user1', password = '123')
#         category = GoodsCategory.objects.create(name="category", category_type = 1)
 

#         need = Goods.objects.create(property_type=0,category=category,emergency=5,user=user,name='need')

#         provide = Goods.objects.create(property_type=1,category=category,emergency=5,user=user,name='provide')

#       #----------测试是否成功创建---------------
#         self.assertTrue(need is not None)
#         self.assertTrue(provide is not None)

#       #----------测试所属用户是否正常------------------
#         self.assertEqual(need.user, user)
#         self.assertEqual(provide.user, user)
      
#       #-------------------测试物品种类和属性-------------
#         self.assertEqual(need.category, category)
#         self.assertEqual(provide.category, category)
#         self.assertEqual(need.property_type, 0)
#         self.assertEqual(provide.property_type, 1)


#       #---------------测试缺省值是否为空----------------
#         self.assertEqual(need.address, '')
#         self.assertEqual(need.goods_brief, '')
#         self.assertEqual(need.goods_desc, '')

# class CategoryViewsetTest(TestCase):
#    def setUp(self):
#       topCategory = GoodsCategory.objects.create(name="topcategory", category_type = 1)

#       secondCategory = GoodsCategory.objects.create(name="secondcategory", category_type = 2, parent_category=topCategory)

#       thirdCategory = GoodsCategory.objects.create(name="thirdcategory", category_type = 3, parent_category=secondCategory)

#       #----------------测试list方法
#    def test_list(self):
#       res = self.client.get('/apis/category/')
#       status_code = res.status_code
#       res_data = res.json()
#       self.assertEqual(status_code, 200)
#       self.assertEqual(res_data.get('count'), 3)

#    #-------------------测试查看特定id的物品类别
#    def test_retrieve(self):
#       topcategory = GoodsCategory.objects.get(name='topcategory')
#       id = topcategory.id
#       res = self.client.get('/apis/category/%d/'%(id))
#       status_code = res.status_code
#       res_data = res.json()
#       self.assertEqual(status_code, 200)
#       self.assertEqual(res_data.get('name'), 'topcategory')


# class NeedsViewsetTest(TestCase):
#    def setUp(self):
#         user = User.objects.create(username = 'user1', password = '123')

#         topCategory = GoodsCategory.objects.create(name="topCategory", category_type = 1)

#         secondCategory = GoodsCategory.objects.create(name="secondCategory", category_type = 2, parent_category=topCategory)


#         category = GoodsCategory.objects.create(name="category", category_type = 3,parent_category=secondCategory)
 

#         need1 = Goods.objects.create(property_type=0,category=category,emergency=5,user=user,name='need1',address='addr',goods_brief="need1")

#         need2 = Goods.objects.create(property_type=0,category=category,emergency=3,user=user,name='need2',address='addr',goods_brief="need2")

#         provide = Goods.objects.create(property_type=1,category=category,emergency=5,user=user,name='provide',address='addr',goods_brief="provide")


#    def test_list(self):
#       res = self.client.get('/apis/goods/')
#       status_code = res.status_code
#       res_data = res.json()
#       self.assertEqual(status_code, 200)
#       self.assertEqual(res_data.get('count'), 2)
#       for good in res_data.get('results'):
#          self.assertNotEqual(good.get('property_type'),1)

#    def test_retrieve(self):
#       need1 = Goods.objects.get(name='need1')
#       id = need1.goods_sn
#       res = self.client.get('/apis/goods/%d/'%(id))
#       status_code = res.status_code
#       res_data = res.json()
#       self.assertEqual(status_code, 200)
#       self.assertEqual(res_data.get('name'), 'need1')


#    #---------------测试按不同层级目录id筛选
#    def test_filter_category(self):
#       top = GoodsCategory.objects.get(name="topCategory")
#       second = GoodsCategory.objects.get(name="secondCategory")
#       third = GoodsCategory.objects.get(name="category")

#       topid = top.id
#       secondid = second.id
#       thirdid = third.id

#       res = self.client.get('/apis/goods/?third_category=%d'%thirdid)
#       res_data = res.json()
#       self.assertEqual(res_data.get('count'), 2)
#       res = self.client.get('/apis/goods/?second_category=%d'%secondid)
#       res_data = res.json()
#       self.assertEqual(res_data.get('count'), 2)
#       res = self.client.get('/apis/goods/?top_category=%d'%topid)
#       res_data = res.json()
#       self.assertEqual(res_data.get('count'), 2)

# class NeedsSearchTest(TestCase):
#    def setUp(self):
#         user = User.objects.create(username = 'user1', password = '123')

#         topCategory = GoodsCategory.objects.create(name="topCategory", category_type = 1)

#         secondCategory = GoodsCategory.objects.create(name="secondCategory", category_type = 2, parent_category=topCategory)


#         category = GoodsCategory.objects.create(name="药品", category_type = 3,parent_category=secondCategory)
 
#         need1 = Goods.objects.create(property_type=0,category=category,emergency=5,user=user,name='莲花清瘟胶囊',address='addr',goods_brief="清热解毒", goods_desc = "清热解毒的莲花清瘟胶囊")
#         need2 = Goods.objects.create(property_type=0,category=category,emergency=3,user=user,name='布洛芬缓释',address='addr',goods_brief="布洛芬缓释胶囊")
#         need3 = Goods.objects.create(property_type=0,category=category,emergency=3,user=user,name='维C银翘',address='addr',goods_desc="维C银翘胶囊")

#    def test_search(self):
#       res = self.client.get('/apis/search/?q=胶囊&page=1')
#       res_data = res.json()
#       names = ['莲花清瘟胶囊', '布洛芬缓释', '维C银翘']
#       goods = [Goods.objects.get(name=i) for i in names]
#       goods_sn_set = set([i.goods_sn for i in goods])  
#       goods_sn_set_search = set()    
#       for good in res_data.get("results"):
#            goods_sn_set_search.add(good.get("goods_sn"))
#       self.assertEqual(goods_sn_set_search, goods_sn_set)
      
           
        
