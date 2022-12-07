from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
# Create your views here.
from goods.models import Goods
from user_operation.models import UserFav, UserLeavingMessage, UserAddress
from user_operation.serializers import UserFavSerializer, UserFavDetailSerializer, LeavingMessageSerializer, \
    AddressSerializer
from rest_framework.permissions import IsAuthenticated
from utils.permissions import IsOwnerOrReadOnly
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication
from goods.serializers import GoodsSerializer


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
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = GoodsSerializer

    def get_queryset(self):
        return Goods.objects.filter(user=self.request.user, property_type=1)

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
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = GoodsSerializer

    def get_queryset(self):
        return Goods.objects.filter(user=self.request.user, property_type=0)
        

class UserFavViewset(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin):
    """
    list:
        获取用户收藏列表
    retrieve:
        判断某个商品是否已经收藏
    create:
        收藏商品
    """
    queryset = UserFav.objects.all()
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    serializer_class = UserFavSerializer
    lookup_field = 'goods_id'
    # lookup_field = 'goods'
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)

    # 收藏数+1
    # def perform_create(self, serializer):
    #     instance = serializer.save()
    #     # 通过这个instance Userfav找到goods
    #     goods = instance.goods
    #     goods.fav_num +=1
    #     goods.save()

    def get_queryset(self):
        return UserFav.objects.filter(user=self.request.user)

    # 设置动态的Serializer
    def get_serializer_class(self):
        if self.action == "list":
            return UserFavDetailSerializer
        elif self.action == "create":
            return UserFavSerializer

        return UserFavSerializer


class LeavingMessageViewset(mixins.ListModelMixin, mixins.DestroyModelMixin, mixins.CreateModelMixin,
                            viewsets.GenericViewSet):
    """
    list:
        获取用户留言
    create:
        添加留言
    delete:
        删除留言功能
    """

    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = LeavingMessageSerializer

    # 只能看到自己的留言
    def get_queryset(self):
        return UserLeavingMessage.objects.filter(user=self.request.user)


class AddressViewset(viewsets.ModelViewSet):
    """
    收货地址管理
    list:
        获取收货地址
    create:
        添加收货地址
    update:
        更新收货地址
    delete:
        删除收货地址
    """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    serializer_class = AddressSerializer

    def get_queryset(self):
        return UserAddress.objects.filter(user=self.request.user)
