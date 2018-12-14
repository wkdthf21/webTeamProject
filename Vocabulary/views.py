from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse, redirect
from django.template import RequestContext, loader
from word.models import Word
from django.contrib.auth.models import User
from .forms import PostForm
import subprocess
from py_translator import Translator
from django.http import HttpResponse

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
    print("add_new_voca")
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


def translate(request):
    print("translate!!!")
    # 로그인 했을 경우
    if 'userId' in request.session:

        userId = request.session['userId']
        print(userId)
        user = User.objects.get(username=userId)

        # 로그인 확인 후 원래 작업
        spell = request.GET.get('spell')
        print(spell)

        #google translate 사용
        '''cmd = ['python']
        result = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).stdout
        output = result.read().strip()
        result.close()
        print(output)'''
        translator = Translator()
        translated = translator.translate(spell, dest='ko')
        print(spell + " : " + translated.text)
        context = {'mean' : translated.text}
        return render(request, 'Vocabulary/translate.html', context)

    # 로그인 안했을 경우
    else:
        redirect_to = reverse('Main')
        return HttpResponseRedirect(redirect_to)

