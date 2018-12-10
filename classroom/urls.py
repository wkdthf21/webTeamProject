from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
     url(r'^(?P<subject_id>\d+)/$', views.Classroom, name='classroom'),

]
#(?P<subject_id>\d+)/$