from . import views
from django.conf.urls import url

urlpatterns = [
    #path('article/', views.show_article),
    #path('post/', views.post_list),
    url(r'^$', views.voca_main, name='voca_main'),
]