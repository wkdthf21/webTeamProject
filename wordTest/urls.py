from django.urls import path
from . import views

urlpatterns =[
   path('', views.test_main , name='test'),
   path('test', views.word_test, name='test'),
]
