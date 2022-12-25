from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from rest_framework.authentication import TokenAuthentication

from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from goods.filters import GoodsFilter
from goods.serializers import GoodsSerializer, CategorySerializer, NeedsHaystackSerializer
from .models import Goods, GoodsCategory
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_haystack.viewsets import HaystackViewSet

# 商品列表分页类


class GoodsPagination(PageNumberPagination):
    page_size = 12
    # 向后台要多少条
    page_size_query_param = 'page_size'
    # 定制多少页的参数
    page_query_param = "page"
    max_page_size = 100

class NeedsSearchView(HaystackViewSet):
    index_models = [Goods]
    serializer_class = NeedsHaystackSerializer

class GoodsCategoryViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    物品类别管理
    list:
        获取物品类别列表
    retrieve:
        获取商品分类详情
    """
    queryset = GoodsCategory.objects.all()
    serializer_class = CategorySerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('category_type','parent_category')

class GoodsListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    需求列表页，分页，搜索，过滤，排序, 取某一个具体需求的详情
    """
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
    queryset = Goods.objects.filter(property_type=0)


    # 设置三大常用过滤器之DjangoFilterBackend, SearchFilter
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # 设置排序
    ordering_fields = ('emergency', 'add_time')
    # 设置filter的类为我们自定义的类
    filter_class = GoodsFilter

    # 设置我们的search字段
    search_fields = ('name', 'goods_brief', 'goods_desc')


