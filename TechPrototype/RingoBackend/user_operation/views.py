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


   #  authentication_classes = (CsrfExemptSessionAuthentication, )
    queryset=Goods.objects.all()
    permission_classes = (IsAuthenticated, )
   #  authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = GoodsSerializer
    
   # def get_queryset(self):
   #    return Goods.objects.filter(user=self.request.user, property_type=1)
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
    # authentication_classes = (CsrfExemptSessionAuthentication, )
    permission_classes = (IsAuthenticated, )
   #  authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = GoodsSerializer
    def create(self, request, *args, **kwargs):
        token = request.META['HTTP_AUTHORIZATION'][5:]
 
        # token = request.META.get('HTTP_AUTHORIZATION', '').replace('Bearer', '').strip()
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

        # token = request.META.get('HTTP_AUTHORIZATION', '').replace('Bearer', '').strip()
        jwtuser = jwt_decode_handler(token)
        data = request.data.copy()
        data['user']=jwtuser["username"]
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

   #  def get_queryset(self):
   #      return Goods.objects.filter(user=self.request.user, property_type=0)
    # def get_queryset(self):
    #    return Goods.objects.filter(property_type=0, user=str(self.request.user)
    def get_queryset(self):
       token = self.request.META['HTTP_AUTHORIZATION'][5:]
       jwtuser = jwt_decode_handler(token)
       print(token)
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
        serializer = PersonalProfileSerializer(profileObj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data)

        else:
            return Response(data=serializer.errors)
