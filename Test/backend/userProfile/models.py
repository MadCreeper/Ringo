from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile():
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=20)
            
