from django.shortcuts import render
from chat.models import Message
from rest_framework import viewsets
from chat.serializers import MessageHistorySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import jwt_decode_handler
from rest_framework import mixins
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
def index(request):
     return render(request, 'chat/index.html', {})
 
def room(request, room_name):
     room_name = room_name
     username = request.GET.get('user', '游客')
     msgs = Message.objects.filter(room=room_name).order_by('create_time')
     print(username)
     return render(request, 'chat/room.html',locals())

class MessageHistoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    物品类别管理
    list:
        获取物品类别列表
    retrieve:
        获取商品分类详情
    """
    queryset = Message.objects.all().order_by('create_time')
    filter_backends = (DjangoFilterBackend,)
    serializer_class = MessageHistorySerializer
    filter_fields = ('room',)
