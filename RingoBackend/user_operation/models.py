from django.db import models
from django.contrib.auth.models import User
from RingoBackend.settings import MEDIA_ROOT
import os
from time import strftime
# Create your models here.
import random
source = "0123456789zxcvbnmasdfghjklqwertyuiopZXCVBNMASDFGHJKLQWERTYUIOP"

def generateCode():
    return ''.join([random.choice(source) for i in range(10)])

def upload_path(instance, filename):
    return '/'.join(['avatar', instance.owner.username, strftime('%Y/%m/%d'), generateCode()+filename[-4:]])

class PersonalProfile(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length = 20, default = "请输入昵称")
    avatar = models.ImageField(upload_to = upload_path, default=os.path.join('default_avatar.png'))
    address = models.CharField(max_length = 255, default = "请输入地址")
    signature = models.CharField(max_length = 255, default = "编辑个性签名")
