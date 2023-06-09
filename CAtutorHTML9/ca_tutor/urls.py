from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views 

app_name = 'ca_tutor'

urlpatterns = [
    path('', views.index, name='index'),
    path('code/', views.code, name='code'),
    path('result/', views.result, name='result'),
]