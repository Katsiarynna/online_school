# chat/endpoints

from rest_framework.views import APIView
from rest_framework import permissions
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet

from .models import Room, Message, ConversationRequest
from .serializers import RoomSerializer, MessageSerializer, ConversationRequestSerializer


def room(request, room_name):
    room_object = get_object_or_404(Room, name=room_name)
    messages = Message.objects.filter(room=room_object)
    return render(request, 'chat/room.html', {'room_name': room_name, 'messages': messages})


class RoomViewSet(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [permissions.IsAuthenticated]


class ConversationRequestViewSet(ModelViewSet):
    queryset = ConversationRequest.objects.all()
    serializer_class = ConversationRequestSerializer
    permission_classes = [permissions.IsAuthenticated]


def get(request):
    user = request.user
    messages = Message.objects.filter(user=user)
    serializer = MessageSerializer(messages, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @staticmethod
    def post(request):
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MessageAPIView(APIView):
    queryset = []
    permission_classes = [permissions.IsAuthenticated]
