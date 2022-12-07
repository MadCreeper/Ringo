from rest_framework import serializers
from login.models import  User

import re

## 实现对象的序列化
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'email', 'password']



class HelperSerializer(serializers.ModelSerializer):
    veriCode = serializers.CharField()

    class Meta:
        model = User
        fields = ['id','username', 'email', 'password', 'veriCode']
    