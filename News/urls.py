from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    #path('article/', views.show_article),
    path('post/', views.post_list),
]