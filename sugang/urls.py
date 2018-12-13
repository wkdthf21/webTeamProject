from django.urls import path, include

from . import views
from django.views.static import serve
from django.conf import settings
from django.conf.urls import url
urlpatterns = [
     path('', views.SugangMain, name='SugangMain'),
     path('addclass/', views.SugangAddNewClass, name='SugangAddNewClass'),
     path('signInstructor/', views.SignInstructor, name='Sign,Instructor'),
     path('thanks/', views.thanks, name='Thanks'),
     path('myclass/', views.myclass, name='Myclass'),
]


#(?P<subject_id>\d+)/$