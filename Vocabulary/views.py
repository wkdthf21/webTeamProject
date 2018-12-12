from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse, redirect
from .models import *
from word.models import Word
from django.contrib.auth.models import User
from .forms import PostForm

# Create your views here.


def voca_main(request):
    # 로그인 했을 경우
    if 'userId' in request.session:

        userId = request.session['userId']
        print(userId)

        #로그인 확인 후 원래 작업
        return render(request, 'Vocabulary/voca_main.html')

    # 로그인 안했을 경우
    else:
        redirect_to = reverse('Main')
        return HttpResponseRedirect(redirect_to)


def word_delete(request):
    spell = request.GET.get("spell")
    print(spell)

    word = Word.objects.filter(word_spell=spell)
    word.delete()

    userId = request.session['userId']
    user = User.objects.get(username=userId)
    vocas = Word.objects.filter(u_id=user)
    return render(request, 'Vocabulary/voca_list.html', {'vocas': vocas})


def my_vocabulary(request):
    # 로그인 했을 경우
    if 'userId' in request.session:

        userId = request.session['userId']
        print(userId)

        #로그인 확인 후 원래 작업
        user = User.objects.get(username=userId)
        vocas = Word.objects.filter(u_id=user)
        return render(request, 'Vocabulary/voca_list.html', {'vocas': vocas})

    # 로그인 안했을 경우
    else:
        redirect_to = reverse('Main')
        return HttpResponseRedirect(redirect_to)


def add_new_voca(request):
    # 로그인 했을 경우
    if 'userId' in request.session:

        userId = request.session['userId']
        print(userId)
        user = User.objects.get(username=userId)

        #로그인 확인 후 원래 작업
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                word = form.save(commit=False)
                word.u_id = user
                word.save()
                return redirect('my_vocabulary')
        else:
            form = PostForm()
        return render(request, 'Vocabulary/add_voca.html', {'form': form})

    # 로그인 안했을 경우
    else:
        redirect_to = reverse('Main')
        return HttpResponseRedirect(redirect_to)


