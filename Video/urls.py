from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('list/', views.VideoList, name = 'ViedoList'),
    path('mainTest/', views.Test_VideoMain, name = 'Test_VideoMain'),
    path('captionTest/', views.Test_VideoCaption, name='Test_VideoCaption'),
    # YouTube
    path('index/', views.index, name='index'),
    path('authorize/', views.authorize, name='authorize'),
    path('oauth2callback/', views.oauth2callback, name='oauth2callback'),
]
