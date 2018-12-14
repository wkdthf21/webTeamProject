from django.urls import path, include
from django.conf.urls import url
from . import views
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
     url(r'^(?P<subject_id>\d+)/$', views.Classroom, name='classroom'),
     url(r'^(?P<subject_id>\d+)/upload/$',  views.Upload, name='upload'),
     path('uploaded/', views.Uploaded, name='uploaded'),
     url(r'^(?P<subject_id>\d+)/(?P<board_id>\d+)/$', views.Open, name='open'),
     url(r'^(?P<subject_id>\d+)/(?P<board_id>\d+)/delete$', views.Delete, name='delete'),
     path('', views.Enter, name='enterclass'),

]
