from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from rest_framework.authentication import TokenAuthentication


from rest_framework.pagination import PageNumberPagination


from goods.filters import GoodsFilter
from goods.serializers import GoodsSerializer, CategorySerializer, NeedsHaystackSerializer
from .models import Goods, GoodsCategory
from rest_framework import mixins, generics
from rest_framework import viewsets
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_haystack.viewsets import HaystackViewSet
from haystack.views import SearchView
from django.http import JsonResponse  

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
# from haystack.views import SearchView


class MySearchView(SearchView):
    '''重写SearchView类'''
    # 指明每页显示 3个
    results_per_page = 5

    # 重写 父类  create_response == >JsonResponse
    def create_response(self):

        # 搜索引擎 给我的数据
        context = self.get_context()

        page = context.get('page')
        object_list = page.object_list
        data_list = []
        all_pages = context['page'].paginator.num_pages
        for good in object_list:
            serializer = GoodsSerializer(good.object)
            data_list.append(serializer.data)
        # 因为前端向后端要前一页和后一页的地址，所以手动传给前端
        text = context.get('query')
        if int(page.number) < int(all_pages):
            # next = f'http://127.0.0.1:8000/article/-1/channel/?page={str(int(page.number) + 1)}'
            next = f'http://127.0.0.1:8000/apis/search/?q={text}&page={str(int(page.number) + 1)}'
        else:
            next = None
        if int(page.number) > 1:
            previous = f'http://127.0.0.1:8000/apis/search/?q={text}&page={str(int(page.number) - 1)}'
        else:
            previous = None
        # return JsonResponse(data_list, safe=False)
        return JsonResponse({'count': len(context), 'next': next, 'previous': previous, 'results': data_list})

class GoodsCategoryViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    物品类别管理
    list:
        获取物品类别列表
    retrieve:
        获取商品分类详情
    """
    queryset = GoodsCategory.objects.all().order_by('id')
    serializer_class = CategorySerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('category_type','parent_category')

class GoodsListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    需求列表页，分页，搜索，过滤，排序, 取某一个具体需求的详情
    """
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
    queryset = Goods.objects.filter(property_type=0).order_by('goods_sn')


    # 设置三大常用过滤器之DjangoFilterBackend, SearchFilter
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # 设置排序
    ordering_fields = ('emergency', 'add_time')
    # 设置filter的类为我们自定义的类
    filter_class = GoodsFilter

    # 设置我们的search字段
    search_fields = ('name', 'goods_brief', 'goods_desc')


