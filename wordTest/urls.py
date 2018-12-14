from django.urls import path
from . import views

urlpatterns =[
   path('', views.test_main , name='TestMain'),
   path('test', views.word_test, name='test'),
   path('result', views.result, name='result'),
   path('review', views.review, name='review'),
]
