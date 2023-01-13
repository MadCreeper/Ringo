from rest_framework import serializers
from login.models import  User

import re

## 实现对象的序列化
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'email', 'password']



## 以下供API调试使用

class HelperSerializer(serializers.ModelSerializer):
    veriCode = serializers.CharField()
    
    class Meta:
        model = User
        fields = ['id','username', 'email', 'password', 'veriCode']

class HelperSerializer2(serializers.ModelSerializer):
    veriCode = serializers.CharField()

    class Meta:
        model = User
        fields = ['email', 'password', 'veriCode']


