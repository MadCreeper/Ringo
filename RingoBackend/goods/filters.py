# -*- coding:utf-8 _*-
from django.db.models import Q
from django_filters import rest_framework as filters
from goods.models import Goods, GoodsCategory
from django.utils.translation import ugettext_lazy as _


class GoodsFilter(filters.FilterSet):
    """
    商品的过滤类
    """
    # 指定字段以及字段上的行为，在shop_price上大于等于
    top_category = filters.NumberFilter(field_name="category", method='top_category_filter')
    second_category = filters.NumberFilter(field_name="category", method='second_category_filter')
    third_category = filters.NumberFilter(field_name="category", method='third_category_filter')

    def top_category_filter(self, queryset, name, value):
        # 不管当前点击的是一级目录二级目录还是三级目录。
        return queryset.filter(Q(category_id=value) | Q(category__parent_category_id=value) | Q(
            category__parent_category__parent_category_id=value))
    def second_category_filter(self, queryset, name, value):
        # 二级目录或三级目录。
        return queryset.filter(Q(category_id=value) | Q(category__parent_category_id=value))
    def third_category_filter(self, queryset, name, value):
        # 三级目录。
        return queryset.filter(Q(category_id=value))

    class Meta:
        model = Goods
        fields = []

# class CategoryFilter(filters.FilterSet):
#     """
#     商品的过滤类
#     """
#     top_category = filters.NumberFilter(field_name="category_type", method='top_category_filter')
#     second_category = filters.NumberFilter(field_name="category", method='second_category_filter')
#     third_category = filters.NumberFilter(field_name="category", method='third_category_filter')

#     def top_category_filter(self, queryset, name, value):
#         # 不管当前点击的是一级目录二级目录还是三级目录。
#         return queryset.filter(Q(category_id=value) | Q(category__parent_category_id=value) | Q(
#             category__parent_category__parent_category_id=value))
#     def second_category_filter(self, queryset, name, value):
#         # 二级目录或三级目录。
#         return queryset.filter(Q(category_id=value) | Q(category__parent_category_id=value))
#     def third_category_filter(self, queryset, name, value):
#         # 三级目录。
#         return queryset.filter(Q(category_id=value))

#     class Meta:
#         model = GoodsCategory
#         fields = []