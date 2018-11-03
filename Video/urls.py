from django.conf.urls import url
from . import views

urlpatterns = [
    path('/list', views.ViedoList, name = 'ViedoList'),
]
