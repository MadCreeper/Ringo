from django.test import TestCase
from django.contrib.auth.models import User
from chat.models import Message
from websocket import create_connection, WebSocketException
import json
import os
from asyncio import new_event_loop
from websockets import connect
from chat.consumers import ChatConsumer
from channels.testing import WebsocketCommunicator
from asgiref.sync import async_to_sync, sync_to_async

# Create your tests here.
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



