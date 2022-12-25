# encoding: utf-8
from chat.models import Message
from rest_framework import serializers

class MessageHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"












