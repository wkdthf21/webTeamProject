"""webTeamProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    #path('account/', include('accounts.urls')),
    path('classroom/', include('classroom.urls')),
    #path('Main/', include('Main.urls')),
    #path('News/', include('News.urls')),
    path('sugang/', include('sugang.urls')),
    #path('Video/', include('Video.urls')),
    #path('Vocabulary/', include('Vocabulary.urls')),
=======
    path('News/', include('News.urls')),
    path('', include('Main.urls')),
    path('account/', include('accounts.urls')),
    #path('classroom/', include('classroom.urls')),
    path('Main/', include('Main.urls')),
    #path('sugang/', include('sugang.urls')),
    path('Vocabulary/', include('Vocabulary.urls')),
    path('Video/', include('Video.urls')),
>>>>>>> ccca456816a81361360a1da1e93cd0b8b8f23f8b
    #path('word/', include('word.urls')),
    path('test/', include('wordTest.urls')),
]
