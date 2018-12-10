from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
     path('', views.SugangMain, name='SugangMain'),
     path('addclass/', views.SugangAddNewClass, name='SugangAddNewClass'),
     path('signInstructor/', views.SignInstructor, name='Sign,Instructor'),
     path('thanks/', views.thanks, name='Thanks'),
     path('myclass/', views.myclass, name='Myclass'),
]
#(?P<subject_id>\d+)/$