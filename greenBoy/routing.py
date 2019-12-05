# chat/routing.py
from django.urls import path

from .consumers import GraphConsumer

websocket_urlpatterns = [
    path('ws/dash', GraphConsumer),
]