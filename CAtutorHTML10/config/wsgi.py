"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
import socketio
import eventlet
import eventlet.wsgi
from django.contrib.staticfiles.handlers import StaticFilesHandler
from ca_tutor.views import sio

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")
django_app = StaticFilesHandler(get_wsgi_application())
application = socketio.Middleware(sio, wsgi_app=django_app, socketio_path='socket.io')

eventlet.wsgi.server(eventlet.listen(('', 8080)), application)