from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    url('^', include('django.contrib.auth.urls')),
    url(r'^join/$', views.signup, name='Join'),
    url(r'^login/$', views.signin, name='Login'),
]
