from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    # path('list/', views.VideoList, name = 'ViedoList'),
    path('mainTest/', views.Test_VideoMain, name = 'Test_VideoMain'),
]
