from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls import url

urlpatterns = [
    #path('article/', views.show_article),
    #path('post/', views.post_list),
    url(r'^$', views.article_list, name='article_list'),
    url(r'^article/(?P<pk>\d+)/$', views.article_detail, name='article_detail'),
    url(r'^article/vocabulary/(?P<fk>\d+)/$', views.article_voca, name='article_voca'),
]