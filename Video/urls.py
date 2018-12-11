from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('list/', views.VideoList, name = 'VideoList'),
    path('add/', views.addVideo, name='addVideo'),
    path('process_addVideo', views.process_addVideo, name = 'process_addVideo'),
    url(r'^main/(?P<video_id>\d+)/$', views.VideoMain),
    url(r'^main/caption/(?P<video_id>\d+)/$', views.VideoCaption),
    path('mainTest/', views.Test_VideoMain, name = 'Test_VideoMain'),
    ### YouTube ###
#    path('index/', views.index, name='index'),
#    path('authorize/', views.authorize, name='authorize'),
#    path('oauth2callback/', views.oauth2callback, name='oauth2callback'),
    ###############
]
