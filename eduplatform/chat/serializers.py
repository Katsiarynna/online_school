from rest_framework import serializers
from .models import Message, ConversationRequest, Room


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


class ConversationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConversationRequest
        fields = "__all__"
