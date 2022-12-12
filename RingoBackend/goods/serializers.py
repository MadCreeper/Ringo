# encoding: utf-8
from django.db.models import Q
from goods.models import Goods, GoodsCategory
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"



class GoodsSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Goods
        fields = "__all__"








