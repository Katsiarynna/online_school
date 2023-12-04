from django.urls import re_path, include
from . import views

urlpatterns = [
    re_path('', views.index_view, name='chat-index'),
    re_path('<str:room_name>/', views.room_view, name='chat-room'),
]
