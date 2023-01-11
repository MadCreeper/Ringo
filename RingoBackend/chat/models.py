from django.db import models

# Create your models here.

class Message(models.Model):
    from_user = models.CharField(max_length=255,verbose_name="发送用户名")
    to_user = models.CharField(max_length=255,verbose_name="接收用户名")
    room = models.CharField(max_length=255,verbose_name="聊天组号")
    content = models.TextField(verbose_name="内容")
    create_time = models.DateTimeField(auto_now_add=True,verbose_name="写入时间")

class ChatGroups(models.Model):
    cur_user =  models.CharField(max_length=255,verbose_name="当前用户")
    chat_user =  models.CharField(max_length=255,verbose_name="当前用户的聊天对象")
    room_name =  models.CharField(max_length=255,verbose_name="房间名")
    unread_messages =  models.IntegerField(default=0,verbose_name="未读消息数")