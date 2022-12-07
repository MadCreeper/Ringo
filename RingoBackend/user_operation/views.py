from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
# Create your views here.
from goods.models import Goods
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from goods.serializers import GoodsSerializer

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
    def get_queryset(self):
       return Goods.objects.filter(property_type=1, user=str(self.request.user))


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

   #  def get_queryset(self):
   #      return Goods.objects.filter(user=self.request.user, property_type=0)
    def get_queryset(self):
       return Goods.objects.filter(property_type=0, user=str(self.request.user))