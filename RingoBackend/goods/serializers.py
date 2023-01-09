# encoding: utf-8
from django.db.models import Q
from goods.models import Goods, GoodsCategory
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from .search_indexes import NeedsIndex
from drf_haystack.serializers import HaystackSerializer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"



class GoodsSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Goods
        fields = "__all__"

class NeedsHaystackSerializer(HaystackSerializer):
   
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    class Meta:
        index_classes = [NeedsIndex]
        fields = ['name', 'goods_brief', 'goods_desc', "goods_sn"]






