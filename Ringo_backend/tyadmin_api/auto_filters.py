from django_filters import rest_framework as filters
from tyadmin_api.custom import DateFromToRangeFilter
from django.contrib.auth.models import Permission, Group
from django.contrib.contenttypes.models import ContentType
from users.models import UserProfile, VerifyCode
from goods.models import GoodsCategory, Goods
from user_operation.models import UserFav, UserAddress, UserLeavingMessage

class PermissionFilter(filters.FilterSet):
    content_type_text = filters.CharFilter(field_name="content_type")

    class Meta:
        model = Permission
        exclude = []

class GroupFilter(filters.FilterSet):

    class Meta:
        model = Group
        exclude = []

class ContentTypeFilter(filters.FilterSet):

    class Meta:
        model = ContentType
        exclude = []

class UserProfileFilter(filters.FilterSet):
    last_login = DateFromToRangeFilter(field_name="last_login")
    date_joined = DateFromToRangeFilter(field_name="date_joined")

    class Meta:
        model = UserProfile
        exclude = []

class VerifyCodeFilter(filters.FilterSet):
    add_time = DateFromToRangeFilter(field_name="add_time")

    class Meta:
        model = VerifyCode
        exclude = []

class GoodsCategoryFilter(filters.FilterSet):
    parent_category_text = filters.CharFilter(field_name="parent_category")
    add_time = DateFromToRangeFilter(field_name="add_time")

    class Meta:
        model = GoodsCategory
        exclude = []

class GoodsFilter(filters.FilterSet):
    category_text = filters.CharFilter(field_name="category")
    user_text = filters.CharFilter(field_name="user")
    add_time = DateFromToRangeFilter(field_name="add_time")

    class Meta:
        model = Goods
        exclude = []

class UserFavFilter(filters.FilterSet):
    user_text = filters.CharFilter(field_name="user")
    goods_text = filters.CharFilter(field_name="goods")
    add_time = DateFromToRangeFilter(field_name="add_time")

    class Meta:
        model = UserFav
        exclude = []

class UserAddressFilter(filters.FilterSet):
    user_text = filters.CharFilter(field_name="user")
    add_time = DateFromToRangeFilter(field_name="add_time")

    class Meta:
        model = UserAddress
        exclude = []

class UserLeavingMessageFilter(filters.FilterSet):
    user_text = filters.CharFilter(field_name="user")
    add_time = DateFromToRangeFilter(field_name="add_time")

    class Meta:
        model = UserLeavingMessage
        exclude = ["file"]