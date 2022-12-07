
from rest_framework import viewsets
from tyadmin_api.custom import XadminViewSet
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from users.models import UserProfile, VerifyCode
from goods.models import GoodsCategory, Goods
from user_operation.models import UserFav, UserAddress, UserLeavingMessage

from tyadmin_api.auto_serializers import PermissionListSerializer, GroupListSerializer, ContentTypeListSerializer, UserProfileListSerializer, VerifyCodeListSerializer, GoodsCategoryListSerializer, GoodsListSerializer, UserFavListSerializer, UserAddressListSerializer, UserLeavingMessageListSerializer
from tyadmin_api.auto_serializers import PermissionCreateUpdateSerializer, GroupCreateUpdateSerializer, ContentTypeCreateUpdateSerializer, UserProfileCreateUpdateSerializer, VerifyCodeCreateUpdateSerializer, GoodsCategoryCreateUpdateSerializer, GoodsCreateUpdateSerializer, UserFavCreateUpdateSerializer, UserAddressCreateUpdateSerializer, UserLeavingMessageCreateUpdateSerializer
from tyadmin_api.auto_filters import PermissionFilter, GroupFilter, ContentTypeFilter, UserProfileFilter, VerifyCodeFilter, GoodsCategoryFilter, GoodsFilter, UserFavFilter, UserAddressFilter, UserLeavingMessageFilter

    
class PermissionViewSet(XadminViewSet):
    serializer_class = PermissionListSerializer
    queryset = Permission.objects.all().order_by('-pk')
    filter_class = PermissionFilter
    search_fields = ["name","codename"]

    def get_serializer_class(self):
        if self.action == "list":
            return PermissionListSerializer
        else:
            return PermissionCreateUpdateSerializer

    
class GroupViewSet(XadminViewSet):
    serializer_class = GroupListSerializer
    queryset = Group.objects.all().order_by('-pk')
    filter_class = GroupFilter
    search_fields = ["name"]

    def get_serializer_class(self):
        if self.action == "list":
            return GroupListSerializer
        else:
            return GroupCreateUpdateSerializer

    
class ContentTypeViewSet(XadminViewSet):
    serializer_class = ContentTypeListSerializer
    queryset = ContentType.objects.all().order_by('-pk')
    filter_class = ContentTypeFilter
    search_fields = ["app_label","model"]

    def get_serializer_class(self):
        if self.action == "list":
            return ContentTypeListSerializer
        else:
            return ContentTypeCreateUpdateSerializer

    
class UserProfileViewSet(XadminViewSet):
    serializer_class = UserProfileListSerializer
    queryset = UserProfile.objects.all().order_by('-pk')
    filter_class = UserProfileFilter
    search_fields = ["password","username","first_name","last_name","name","gender","mobile","email"]

    def get_serializer_class(self):
        if self.action == "list":
            return UserProfileListSerializer
        else:
            return UserProfileCreateUpdateSerializer

    
class VerifyCodeViewSet(XadminViewSet):
    serializer_class = VerifyCodeListSerializer
    queryset = VerifyCode.objects.all().order_by('-pk')
    filter_class = VerifyCodeFilter
    search_fields = ["code","mobile"]

    def get_serializer_class(self):
        if self.action == "list":
            return VerifyCodeListSerializer
        else:
            return VerifyCodeCreateUpdateSerializer

    
class GoodsCategoryViewSet(XadminViewSet):
    serializer_class = GoodsCategoryListSerializer
    queryset = GoodsCategory.objects.all().order_by('-pk')
    filter_class = GoodsCategoryFilter
    search_fields = ["name","code"]

    def get_serializer_class(self):
        if self.action == "list":
            return GoodsCategoryListSerializer
        else:
            return GoodsCategoryCreateUpdateSerializer

    
class GoodsViewSet(XadminViewSet):
    serializer_class = GoodsListSerializer
    queryset = Goods.objects.all().order_by('-pk')
    filter_class = GoodsFilter
    search_fields = ["goods_sn","name"]

    def get_serializer_class(self):
        if self.action == "list":
            return GoodsListSerializer
        else:
            return GoodsCreateUpdateSerializer

    
class UserFavViewSet(XadminViewSet):
    serializer_class = UserFavListSerializer
    queryset = UserFav.objects.all().order_by('-pk')
    filter_class = UserFavFilter
    search_fields = []

    def get_serializer_class(self):
        if self.action == "list":
            return UserFavListSerializer
        else:
            return UserFavCreateUpdateSerializer

    
class UserAddressViewSet(XadminViewSet):
    serializer_class = UserAddressListSerializer
    queryset = UserAddress.objects.all().order_by('-pk')
    filter_class = UserAddressFilter
    search_fields = ["province","city","district","address","signer_name","signer_mobile"]

    def get_serializer_class(self):
        if self.action == "list":
            return UserAddressListSerializer
        else:
            return UserAddressCreateUpdateSerializer

    
class UserLeavingMessageViewSet(XadminViewSet):
    serializer_class = UserLeavingMessageListSerializer
    queryset = UserLeavingMessage.objects.all().order_by('-pk')
    filter_class = UserLeavingMessageFilter
    search_fields = ["subject"]

    def get_serializer_class(self):
        if self.action == "list":
            return UserLeavingMessageListSerializer
        else:
            return UserLeavingMessageCreateUpdateSerializer
