from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from login.models import User
from login.serializer import UserSerializer, HelperSerializer
import json
import login.helpers.codeGenerator, login.helpers.mailSend
import datetime
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.hashers import make_password
# Create your views here.
# Constants
ERR_REG_USERNAME_EXIST = 1001
ERR_REG_EMAIL_EXIST = 1002
ERR_REG_WRONG_VERIFICATION = 1003
ERR_REG_VERIFICATION_REQUEST_TOO_FREQUENT = 1004

ERR_LOGIN_USER_NOT_EXIST = 2001
ERR_LOGIN_WRONG_PWD = 2002

# stores 
veriCodeHash= {}

class UserRegisterView(APIView):
    # 测试用代码：
    # queryset = User.objects.all()
    # # serializer_class = UserSerializer
    # serializer_class = HelperSerializer

    def post(self, request, format = None):
        dataDict = request.data
        username = dataDict.get('username')
        email = dataDict.get('email')
        if User.objects.filter(username = username):
            # 用户名已存在
            return Response(data={'errorCode':'usernameExists'})
        elif User.objects.filter(email = email):
            # 邮箱已被注册
            return Response(data = {'errorCode':'emailExists'})
        elif not dataDict.get('veriCode'):
            # 未填写验证码信息， 发送验证码
            if veriCodeHash.get(email):
                # 查看验证码是否已经被发送过
                timestamp = veriCodeHash.get(email)[0]
                now = datetime.datetime.now().timestamp()
                delta = now - timestamp
                if delta < 60:
                    # 申请验证码时间过短，不允许
                    return Response(data={'errorCode':'timeTooShort'})
            veriCode = login.helpers.codeGenerator.generateCode()
            veriCodeHash[email] = (datetime.datetime.now().timestamp(), veriCode)
            login.helpers.mailSend.sendMail(reveiver=email, validation=veriCode)
            return Response()
        else:
            veriCode = dataDict.get('veriCode')
            veriCodeStored = veriCodeHash.get(email)
            if not veriCodeStored or veriCodeStored[1] != veriCode:
                # 验证码验证不通过
                return Response()
            veriCodeHash.pop(email)
            mData = {
                'username' : request.data.get('username'),
                'password' : make_password(request.data.get('password')),
                'email' : request.data.get('email')
            }
            serializer = UserSerializer(data=mData)
            if serializer.is_valid():
                serializer.save()
                return Response(data = {}, status = status.HTTP_201_CREATED)
            return Response()



class UserPasswordChangeView(APIView):
    serializer = UserSerializer
    def post(self, request, format = None):
        return Response()