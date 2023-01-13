# encoding: utf-8
from chat.models import Message, ChatGroups
from rest_framework import serializers

class MessageHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"

class ChatGroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatGroups
        fields = "__all__"












