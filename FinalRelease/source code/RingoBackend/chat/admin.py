from django.contrib import admin
from chat.models import Message,  ChatGroups
# Register your models here.
admin.site.register(Message) 
admin.site.register(ChatGroups)