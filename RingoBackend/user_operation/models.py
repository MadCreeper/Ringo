from django.db import models
from django.contrib.auth.models import User
from RingoBackend.settings import MEDIA_ROOT
import os 
# Create your models here.

class PersonalProfile(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length = 20, default = "请输入昵称")
    avatar = models.ImageField(upload_to = 'avatar/%Y/%m/%d', default=os.path.join('default_avatar.png'))
    address = models.CharField(max_length = 255, default = "请输入地址")
    signature = models.CharField(max_length = 255, default = "编辑个性签名")
