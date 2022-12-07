from rest_framework import serializers
from login.models import RingoUser, LANGUAGE_CHOICES, STYLE_CHOICES
import re


class RingoUserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=RingoUser
        fields = ['username', 'password','email']
    
    def validate_username(self, username):
        if RingoUser.objects.filter(username = username).count():
            raise serializers.ValidationError("用户名已经存在")
        return username
    
    def validate_email(self, email):
        if RingoUser.objects.filter(email = email).count():
            raise serializers.ValidationError("邮箱已经被注册")
        pattern = r"^[a-z0-9A-Z]+[- | a-z0-9A-Z . _]+@sjtu.edu.cn"
        if not re.match(email, pattern = pattern):
            raise serializers.ValidationError("使用的不是交大邮箱")
        return email
    
    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user