from django.shortcuts import render,HttpResponseRedirect, reverse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404
from .models import *
from word.models import *
from django.http import HttpResponse


# Create your views here.


def article_list(request):
    # 로그인 했을 경우
    if 'userId' in request.session:

        userId = request.session['userId']
        print(userId)

        articles = Article.objects.all()
        return render(request, 'News/article_list.html', {'articles': articles})


    # 로그인 안했을 경우
    else:
        redirect_to = reverse('Main')
        return HttpResponseRedirect(redirect_to)


def article_detail(request, pk):
    # 로그인 했을 경우
    if 'userId' in request.session:

        userId = request.session['userId']
        print(userId)

        article = get_object_or_404(Article, pk=pk)
        return render(request, 'News/article_detail.html', {'article': article})

    # 로그인 안했을 경우
    else:
        redirect_to = reverse('Main')
        return HttpResponseRedirect(redirect_to)


def article_voca(request, fk):
    # 로그인 했을 경우
    if 'userId' in request.session:

        userId = request.session['userId']
        print(userId)

        print(fk)
        vocas = ArticleVoca.objects.filter(article_id=fk)
        return render(request, 'News/article_voca.html', {'vocas': vocas, 'article_id': fk})

    # 로그인 안했을 경우
    else:
        redirect_to = reverse('Main')
        return HttpResponseRedirect(redirect_to)


def add_my_voca(request):
    spell = request.GET.get("spell")
    mean = request.GET.get("mean")
    article_id = request.GET.get("article_id")

    userId = request.session['userId']
    print(userId)
    user = User.objects.get(username=userId)

    voca = Word(word_spell=spell, word_mean=mean, u_id=user)
    voca.save()

    vocas = ArticleVoca.objects.filter(article_id=article_id)
    return render(request, 'News/article_voca.html', {'vocas': vocas, 'article_id': article_id})





