from channels.generic.websocket import WebsocketConsumer, AsyncJsonWebsocketConsumer, AsyncWebsocketConsumer
import json
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync, sync_to_async
from django.contrib.auth.models import User
from chat.models import Message
import datetime
from xpinyin import Pinyin

 


class ChatConsumer(WebsocketConsumer):
     def __init__(self, *args, **kwargs):
         super().__init__(*args, **kwargs)
         self.group_id = 0
     
     def save_msg(self,from_user,to_user,room,msg):
        Message.objects.create(from_user=from_user, to_user = to_user, room=room, content=msg)
     # websocket建立连接时执行方法
     def connect(self):
         # 从url里获取聊天室名字，为每个房间建立一个频道组
         p = Pinyin()
         self.room_name = self.scope['url_route']['kwargs']['room_name']
         result = p.get_pinyin(self.room_name,tone_marks='numbers')
         self.room_group_name = ('chat_%s_%d' % (result, hash(result)))
         print("connenting. room_name: %s, group_name:%s"%(self.room_name, self.room_group_name))
 
         # 将当前频道加入频道组
         async_to_sync(self.channel_layer.group_add)(
             self.room_group_name,
             self.channel_name
         )
      
         # 接受所有websocket请求
         self.accept()
 
     # websocket断开时执行方法
     def disconnect(self, close_code):
         async_to_sync(self.channel_layer.group_discard)(
             self.room_group_name,
             self.channel_name
         )
     
 
     # 从websocket接收到消息时执行函数
     def receive(self, text_data):
         text_data_json = json.loads(text_data)
         message = text_data_json['message']
         from_user = text_data_json['from_user']
         to_user =  text_data_json['to_user'] 
         room = text_data_json['room'] 
         self.save_msg(from_user,to_user, room, message)
         # 发送消息到频道组，频道组调用chat_message方法
         async_to_sync(self.channel_layer.group_send)(
             self.room_group_name,
             {
                 'type': 'chat_message',
                 'message': message,
                 'from_user':from_user,
                 'to_user':to_user,
                 'room':room
             }
         )
    
 
     # 从频道组接收到消息后执行方法
     def chat_message(self, event):
         message = event['message']
         from_user = event['from_user']
         to_user =  event['to_user']     
         room =  event['room']  
         datetime_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
 
         # 通过websocket发送消息到客户端
         self.send(text_data=json.dumps({
            #  'message': f'{datetime_str}:{message}',
             'message': message,
             'from_user': from_user,
             'to_user':to_user,
             'time':datetime_str,
             'room':room
         }))
