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
from goods.serializers import GoodsSerializer, CategorySerializer
from .models import Goods, GoodsCategory
from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

# 商品列表分页类


class GoodsPagination(PageNumberPagination):
    page_size = 12
    # 向后台要多少条
    page_size_query_param = 'page_size'
    # 定制多少页的参数
    page_query_param = "page"
    max_page_size = 100


class GoodsCategoryViewset(viewsets.ModelViewSet):
    """
    物品类别管理
    list:
        获取物品类别列表
    create:
        添加物品类别
    update:
        更新物品类别
    delete:
        删除物品类别
    """
    queryset = GoodsCategory.objects.all()
    serializer_class = CategorySerializer

class GoodsListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    需求列表页，分页，搜索，过滤，排序, 取某一个具体需求的详情
    """
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
    queryset = Goods.objects.filter(property_type=0)

    # 设置列表页的单独auth认证也就是不认证
    # authentication_classes = (TokenAuthentication,)

    # 设置三大常用过滤器之DjangoFilterBackend, SearchFilter
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # 设置排序
    ordering_fields = ('emergency', 'add_time')
    # 设置filter的类为我们自定义的类
    filter_class = GoodsFilter

    # 设置我们的search字段
    search_fields = ('name', 'goods_brief', 'goods_desc')


class CategoryViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
        商品分类列表数据
    retrieve:
        获取商品分类详情
    """
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer