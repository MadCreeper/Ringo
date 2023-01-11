from django.test import TestCase
from django.contrib.auth.models import User
from chat.models import Message, ChatGroups
from websocket import create_connection, WebSocketException
import json
import os
from rest_framework import status
from asyncio import new_event_loop
from websockets import connect
from chat.consumers import ChatConsumer
from channels.testing import WebsocketCommunicator
from asgiref.sync import async_to_sync, sync_to_async

# Create your tests here.

class ChatGroupTest(TestCase):
   def get_header(self):
      send_data ={'username':'user1', 'password':'123'}
      res = self.client.post('/apis/login/login', data = send_data)
      res_data = res.json()
      token = res_data.get('token')
      header = 'JWT  ' + token
      return header

   def setUp(self):
      group1 = ChatGroups.objects.create(cur_user='user1',chat_user='user2',room_name='user1_user2')
      group2 = ChatGroups.objects.create(cur_user='user2',chat_user='user1',room_name='user1_user2')
      group3 = ChatGroups.objects.create(cur_user='user1',chat_user='user3',room_name='user1_user3')
      

   def test_group_list(self):
      user1 = User.objects.create_user(username = 'user1', password = '123', email='user1@user1.com')
      header = self.get_header()

      user_set = set(('user2', 'user3'))
      group1 = self.client.get('/apis/group_user/', HTTP_AUTHORIZATION = header)
      res_data_1 = group1.json()
      set_res = set()
      for data in res_data_1.get('results'):
         set_res.add(data['chat_user'])
      self.assertEqual(set_res, user_set)

   def test_init_zero(self):
      group1 = ChatGroups.objects.get(cur_user='user1', chat_user ='user2')
      self.assertEqual(group1.unread_messages, 0)

   def test_msg_reset(self):
      user1 = User.objects.create_user(username = 'user1', password = '123', email='user1@user1.com')
      header = self.get_header()
      send_data ={'cur_user':'user1', 'chat_user':'user2'}
      res = self.client.post('/chat/reset_msg', data = send_data, HTTP_AUTHORIZATION = header)
      group1 = ChatGroups.objects.get(cur_user='user1', chat_user ='user2')
      self.assertEqual(group1.unread_messages, 0)
      group1.unread_messages += 1
      group1.save()
      group1 = ChatGroups.objects.get(cur_user='user1', chat_user ='user2')
      self.assertEqual(group1.unread_messages, 1)
      res = self.client.post('/chat/reset_msg', data = send_data, HTTP_AUTHORIZATION = header)
      group1 = ChatGroups.objects.get(cur_user='user1', chat_user ='user2')
      self.assertEqual(group1.unread_messages, 0)
      send_data['chat_user'] = 'user10086'
      res = self.client.post('/chat/reset_msg', data = send_data, HTTP_AUTHORIZATION = header)
      group1 = ChatGroups.objects.get(cur_user='user1', chat_user ='user10086')
      self.assertEqual(group1.unread_messages, 0)

   def test_msg_add(self):
       user1 = User.objects.create_user(username = 'user1', password = '123', email='user1@user1.com')
       header = self.get_header()
       send_data ={'cur_user':'user1', 'chat_user':'user2'}
       send_data1 ={'cur_user':'user2', 'chat_user':'user1'}
       res = self.client.post('/chat/reset_msg', data = send_data1, HTTP_AUTHORIZATION = header)
       group1 = ChatGroups.objects.get(cur_user='user2', chat_user ='user1')
       self.assertEqual(group1.unread_messages, 0)
       res = self.client.post('/chat/add_msg', data = send_data, HTTP_AUTHORIZATION = header)
       group1 = ChatGroups.objects.get(cur_user='user2', chat_user ='user1')
       self.assertEqual(group1.unread_messages, 1)
       send_data['chat_user'] = 'user114514'
       res = self.client.post('/chat/add_msg', data = send_data, HTTP_AUTHORIZATION = header)
       group1 = ChatGroups.objects.get(cur_user='user114514', chat_user ='user1')
       self.assertEqual(group1.unread_messages, 1)
      
      
      



# class ChatTest(TestCase):
#    def setUp(self):
#       room_name = 'user1_user2'

#       user1 = User.objects.create(username = 'user1', password = '123')
#       user2 = User.objects.create(username = 'user2', password = '123')

#       hisMessage1 = Message.objects.create(from_user = 'user1', to_user = 'user2', room = room_name, content = 'history message 1')
#       hisMessage2 = Message.objects.create(from_user = 'user2', to_user = 'user1', room = room_name, content = 'history message 2')
#       hisMessage3 = Message.objects.create(from_user = 'user1', to_user = 'user2', room = room_name, content = 'history message 3')
#       hisMessage4 = Message.objects.create(from_user = 'user2', to_user = 'user1', room = room_name, content = 'history message 4')


#    async def test_send_and_get_history(self):
#       room_name = 'user1_user2'
#       hisMessages1 = await self.client.get(f'/apis/history/?room={room_name}')
#       communicator = WebsocketCommunicator(ChatConsumer.as_asgi(), f"/ws/chat/{room_name}")
#       connected = communicator.connect()
#       self.assertTrue(connected)


#       message_dict = {
#                   'message': 'send_message_1',
#                   'from_user':'user1',
#                   'to_user':'user2',
#                   'room': room_name
#       }

#       data = json.dumps(message_dict)
#       await communicator.send_to(text_data=data)
#       result = await communicator.receive_from()
#       hisMessages2 = await self.client.get(f'/apis/history/?room={room_name}')
#       res_data_1 = hisMessages1.json()
#       res_data_2 = hisMessages2.json()
#       self.assertEqual(res_data_1.get('count'), 4)
#       self.assertEqual(res_data_2.get('count'), 5)
#       await communicator.disconnect()


#    async def test_send_and_get_messages(self):
#       room_name = 'user1_user2'
#       connect_path = f'ws://127.0.0.1:8000/ws/chat/{room_name}/'
#       communicator = WebsocketCommunicator(ChatConsumer.as_asgi(), f"/ws/chat/{room_name}")
#       connected, subprotocol = await communicator.connect()

#       message_dict = {
#                   'message': 'send_message_1',
#                   'from_user':'user1',
#                   'to_user':'user2',
#                   'room': room_name
#          }
#       await communicator.send_to(text_data=json.dumps(message_dict))
#       recvmsg =  await communicator.receive_from()
#       recvmsg = json.loads(recvmsg)
#       message_dict['time'] = recvmsg['time']
#       self.assertEqual(message_dict, recvmsg)
#       await communicator.disconnect()



   # def test_send_and_get_history(self):
   #    room_name = 'user1_user2'
   #    hisMessages1 = self.client.get(f'/apis/history/?room={room_name}')
   #    connect_path = f'ws://127.0.0.1:8000/ws/chat/{room_name}/'


   #    ws = create_connection(connect_path)

   #    send_data = json.dumps({
   #                'message': 'send_message_1',
   #                'from_user':'user1',
   #                'to_user':'user2',
   #                'room': room_name
   #    })

   #    ws.send(send_data)
  
   #    hisMessages2 = self.client.get(f'/apis/history/?room={room_name}')

   #    res_data_1 = hisMessages1.json()
   #    res_data_2 = hisMessages2.json()

   #    self.assertEqual(res_data_1.get('count'), 4)
   #    self.assertEqual(res_data_2.get('count'), 4)

   # def test_send_and_get_messages(self):
   #    room_name = 'user1_user2'
   #    connect_path = f'ws://127.0.0.1:8000/ws/chat/{room_name}/'


   #    ws = create_connection(connect_path)

   #    message_dict = {
   #                'message': 'send_message_1',
   #                'from_user':'user1',
   #                'to_user':'user2',
   #                'room': room_name
   #       }
   #    ws.send(json.dumps(message_dict))
   #    recvmsg = ws.recv()
   #    recvmsg = json.loads(recvmsg)
   #    message_dict['time'] = recvmsg['time']
   #    self.assertEqual(message_dict, recvmsg)
   #    ws.close()



