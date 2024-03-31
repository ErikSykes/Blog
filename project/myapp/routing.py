# myapp/routing.py

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from myapp.consumers import CommentConsumer


application = ProtocolTypeRouter({
    # WebSocket chat handler
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path("ws/comment/<int:topic_id>/", CommentConsumer.as_asgi()),
            # Add more WebSocket paths as needed
        ])
    ),
})
