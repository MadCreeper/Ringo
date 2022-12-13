"""
ASGI config for RingoBackend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from django.urls import path
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from chat.consumers import ChatConsumer, PushConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RingoBackend.settings')

application = ProtocolTypeRouter({
  "http": get_asgi_application(),
  "websocket": AuthMiddlewareStack(
    URLRouter([
        path("ws/<str:room_name>/",ChatConsumer.as_asgi()),
        path("ws/<str:user>/",PushConsumer.as_asgi()),
      ])
  )
})
