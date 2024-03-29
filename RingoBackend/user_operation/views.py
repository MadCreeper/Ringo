from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
# Create your views here.
from goods.models import Goods
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from goods.serializers import GoodsSerializer
from rest_framework_jwt.authentication import jwt_decode_handler

from rest_framework import status

from user_operation.serializers import PersonalProfileSerializer
from user_operation.models import PersonalProfile
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import QueryDict
from rest_framework.authentication import SessionAuthentication
from login.models import User
import datetime

from user_operation.helpers.item_sorter import *


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return 

class UserOfferingViewset(viewsets.ModelViewSet):
    """
    提供条目管理
    list:
        获取用户提供列表
    create:
        添加提供物品
    update:
        更新提供物品
    delete:
        删除提供物品
    """


    queryset=Goods.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = GoodsSerializer
    
    def create(self, request, *args, **kwargs):
        token = request.META['HTTP_AUTHORIZATION'][5:]
        jwtuser = jwt_decode_handler(token)
        data = request.data.copy()
        data['user']=jwtuser["username"]
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        token = request.META['HTTP_AUTHORIZATION'][5:]
        jwtuser = jwt_decode_handler(token)
        data = request.data.copy()
        data['user']=jwtuser["username"]
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def get_queryset(self):
       token = self.request.META['HTTP_AUTHORIZATION'][5:]
       jwtuser = jwt_decode_handler(token)
       return Goods.objects.filter(property_type=1, user=jwtuser["username"])

class UserNeedsViewset(viewsets.ModelViewSet):
    """
    需求条目管理
    list:
        获取用户需求列表
    create:
        添加需求物品
    update:
        更新需求物品
    delete:
        删除需求物品
    """
    queryset=Goods.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = GoodsSerializer
    def create(self, request, *args, **kwargs):
        token = request.META['HTTP_AUTHORIZATION'][5:]
        jwtuser = jwt_decode_handler(token)
        data = request.data.copy()
        data['user']=jwtuser["username"]
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        token = request.META['HTTP_AUTHORIZATION'][5:]
        jwtuser = jwt_decode_handler(token)
        data = request.data.copy()
        data['user']=jwtuser["username"]
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def get_queryset(self):
       token = self.request.META['HTTP_AUTHORIZATION'][5:]
       jwtuser = jwt_decode_handler(token)
       return Goods.objects.filter(property_type=0, user=jwtuser["username"])

class PersonalProfileView(APIView):
    serializer_class = PersonalProfileSerializer
    permission_classes = (IsAuthenticated, )
    def get(self, request):
        curr_user = request.user
        created = False
        if not PersonalProfile.objects.filter(owner = curr_user):
            created = True
            serializer = PersonalProfileSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(owner = curr_user)
            else:
                return Response(data = {'errorCode': 'Unexpected error.'})
        profileObj = PersonalProfile.objects.get(owner = curr_user)
        serializer = PersonalProfileSerializer(profileObj)
        return Response(data={**serializer.data, 'created' :created})
    
    def post(self, request):
        print(request.data)
        curr_user = request.user
        created = False
        if not PersonalProfile.objects.filter(owner = curr_user):
            created = True
            serializer = PersonalProfileSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(owner = curr_user)
            else:
                return Response(data = {'errorCode': 'Unexpected error.', **serializer.errors})
        profileObj = PersonalProfile.objects.get(owner = curr_user)
        serializer = PersonalProfileSerializer(profileObj, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(data = {**serializer.data, 'test':'saved'})
        else:
            return Response(data={'err':serializer.errors})

class userPhotoView(APIView):
    '''
    建立或断开连接时，将自己的未读消息清空
    '''
    permission_classes = (IsAuthenticated, )
    def get(self, request, format = None):
        username = request.GET["username"]
        print(username)
        cur_user = User.objects.get(username = username)
        profileObj = PersonalProfile.objects.get(owner = cur_user)
        serializer = PersonalProfileSerializer(profileObj)
        mData = {'avatar':serializer.data['avatar']}
        return Response(data = mData, status = status.HTTP_200_OK)


class RecommendationView(APIView):
    '''
    推荐模块的对应API
    '''
    permission_classes = (IsAuthenticated, )
    serializer_class = GoodsSerializer
    result_cache = {}
    PAGE_SIZE = 200

    def create_response(self, id_list, page):
        respData = {'previous':'', 'next':'', 'errorCode':'', 'results':[]}
        if (page-1) * self.PAGE_SIZE > len(id_list):
            respData['errorCode'] = 'Page too large, 当前页面没有可以展示的信息。'
            return Response(data=respData)
        curr_slice = id_list[(page-1)*self.PAGE_SIZE:page*self.PAGE_SIZE]
        
        curr_data = [GoodsSerializer(Goods.objects.get(pk = i)).data for i in curr_slice]
        respData['results'] = curr_data
        if page != 1:
            respData['previous'] = f'/apis/recommend/{page-1}'
        if (page) * self.PAGE_SIZE < len(id_list):
            respData['next'] = f'/apis/recommend/{page+1}'
        return Response(data=respData)
        

    def get(self, request, page = 1):
        curr_user = request.user
        user_offerings = fetch_all_offers(user=curr_user)
        all_needs = fetch_all_needs()
        if not user_offerings:
            # 当前用户没有提供的信息
            id_list = [i.pk for i in all_needs][:200]
            return self.create_response(id_list, page)

        id_list = None
        if curr_user.id not in self.result_cache or \
            datetime.datetime.now().timestamp() - self.result_cache[curr_user.id][0] > 3600:
            curr_tag = get_string_tag(user_offerings)
            sort_by_similarity(all_needs, curr_tag)
            id_list = [i.pk for i in all_needs]
            if len(id_list) > 200: 
                id_list = id_list[:200]
            self.result_cache[curr_user.id] = (datetime.datetime.now().timestamp(), id_list)
        else:
            id_list = self.result_cache[curr_user.id][1]
        
        return self.create_response(id_list, page)


