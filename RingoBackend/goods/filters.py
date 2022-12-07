# -*- coding:utf-8 _*-
from django.db.models import Q
from django_filters import rest_framework as filters
from goods.models import Goods
# from django.utils.translation import ugettext_lazy as _


class GoodsFilter(filters.FilterSet):
    """
    物品的过滤类
    """
    top_category = filters.NumberFilter(field_name="category", method='top_category_filter')


    def top_category_filter(self, queryset,name, value):
        # 不管当前点击的是一级目录二级目录还是三级目录。
        return queryset.filter(Q(category_id=value) | Q(category__parent_category_id=value) | Q(
            category__parent_category__parent_category_id=value))

    class Meta:
        model = Goods
        fields = ['name']
