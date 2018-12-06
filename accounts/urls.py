from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^join/$', views.signup, name='Join'),
    url(r'^login/$', views.signin, name='Login'),
    url(r'^logout/$', views.signout, name='Logout'),
]
