# encoding: utf-8
from django.db.models import Q
from goods.models import Goods
from rest_framework import serializers


# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = GoodsCategory
#         fields = "__all__"



class GoodsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Goods
        fields = "__all__"






