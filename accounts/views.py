from django.shortcuts import render,reverse, HttpResponseRedirect, redirect
from django.http import HttpResponse
from Main import urls
from .models import *
from .forms import UserForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.template import RequestContext


# Create your views here.

# 회원가입 view
def signup(request):

    if request.method == "POST":

        form = UserForm(request.POST)

        # 회원가입 성공
        if form.is_valid():

            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)

            return redirect('../login/')
        # 회원가입 실패
        else:
            return HttpResponse('회원가입 실패!')

    # 회원가입 template
    else:
        form = UserForm()
        return render(request, 'join.html', {'form': form})

# 로그인 view
def signin(request):

    if request.method == "POST":

        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)

        # 로그인 성공
        if user is not None:
            login(request, user)
            redirect_to = reverse('Main')
            return HttpResponseRedirect(redirect_to)

        # 로그인 실패
        else:
            return HttpResponse('로그인 실패!')

    # 로그인 teamplate
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
