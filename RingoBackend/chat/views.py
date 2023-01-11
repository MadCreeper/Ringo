from django.shortcuts import render
from chat.models import Message, ChatGroups
from rest_framework import viewsets
from rest_framework.views import APIView
from chat.serializers import MessageHistorySerializer, ChatGroupsSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import jwt_decode_handler
from rest_framework import mixins
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status


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
    历史信息管理
    """
    permission_classes = (IsAuthenticated, )
    queryset = Message.objects.all().order_by('create_time')
    filter_backends = (DjangoFilterBackend,)
    serializer_class = MessageHistorySerializer
    filter_fields = ('room',)
    def get_queryset(self):
       token = self.request.META['HTTP_AUTHORIZATION'][5:]
       jwtuser = jwt_decode_handler(token)
       return Message.objects.filter(cur_user=jwtuser["username"])

class ChatGroupsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    聊天对象管理
    """
    permission_classes = (IsAuthenticated, )
    queryset = ChatGroups.objects.all().order_by('-unread_messages')
    filter_backends = (DjangoFilterBackend,)
    serializer_class = ChatGroupsSerializer
    def get_queryset(self):
       token = self.request.META['HTTP_AUTHORIZATION'][5:]
       jwtuser = jwt_decode_handler(token)
       return ChatGroups.objects.filter(cur_user=jwtuser["username"])



class resetMsgView(APIView):
    '''
    建立或断开连接时，将自己的未读消息清空
    '''
    permission_classes = (IsAuthenticated, )
    def post(self, request, format = None):
        cur_user = request.user.username
        chat_user = request.data.get('chat_user')
        room_name = min(cur_user, chat_user) + '_' + max(cur_user, chat_user)
        try:
            chat_msg_data = ChatGroups.objects.get(cur_user = cur_user, chat_user=chat_user)
        except:
            chat_msg_data = None
        mData = {'unread_messages':0, 'cur_user':cur_user, 'chat_user':chat_user, 'room_name':room_name}
        if not chat_msg_data:
            chat_msg_data = ChatGroups(unread_messages = 0, cur_user = cur_user, chat_user = chat_user, room_name = room_name)
        else:
            chat_msg_data.unread_messages = 0
        chat_msg_data.save()
        return Response(data = mData, status = status.HTTP_200_OK)

class addUnreadMsgView(APIView):
    '''
    发送消息时，给对方增加未读消息
    '''
    permission_classes = (IsAuthenticated, )
    def post(self, request, format = None):
        cur_user = request.user.username
        chat_user = request.data.get('chat_user')
        room_name = min(cur_user, chat_user) + '_' + max(cur_user, chat_user)
        try:
            chat_msg_data = ChatGroups.objects.get(cur_user = chat_user, chat_user=cur_user)
        except:
            chat_msg_data = None
        new_msgs = 0
        if not chat_msg_data:
            chat_msg_data = ChatGroups(unread_messages = 1, cur_user = chat_user, chat_user = cur_user, room_name = room_name)
            new_msgs = 0
        else:
            chat_msg_data.unread_messages += 1
            new_msgs = chat_msg_data.unread_messages
        mData = {'unread_messages':new_msgs, 'cur_user':chat_user, 'chat_user':cur_user, 'room_name':room_name}
        chat_msg_data.save()
        return Response(data = mData, status = status.HTTP_200_OK)


