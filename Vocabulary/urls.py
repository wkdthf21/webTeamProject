from . import views
from django.conf.urls import url
from django.urls import path

urlpatterns = [
    #path('article/', views.show_article),
    #path('post/', views.post_list),
    url(r'^$', views.voca_main, name='voca_main'),
    url(r'^my-vocabulary/$', views.my_vocabulary, name='my_vocabulary'),
    url(r'^my-vocabulary/add-new/$', views.add_new_voca, name='add_new_voca'),
    url(r'^my-vocabulary/delete$', views.word_delete, name='word_delete'),
    url(r'^my-vocabulary/add-new/translate/$', views.translate, name='translate'),
    #path('^my-vocabulary/delete/<spell>/$', views.word_delete, name="word_delete"),
]