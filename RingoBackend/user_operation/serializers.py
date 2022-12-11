from rest_framework import serializers
from login.models import  User
from user_operation.models import PersonalProfile

class PersonalProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # owner_id = serializers.IntegerField(source='owner.id')

    class Meta:
        model = PersonalProfile
        fields = ['owner', 'nickname', 'avatar', 'address', 'signature']
    
    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)