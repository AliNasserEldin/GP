"""
ASGI config for GP project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django_channels_jwt_auth_middleware.auth import JWTAuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from chat.routing import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GP.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    "websocket": JWTAuthMiddlewareStack(URLRouter(websocket_urlpatterns))
}) 
