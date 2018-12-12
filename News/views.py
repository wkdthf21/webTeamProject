from django.shortcuts import render,HttpResponseRedirect, reverse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, get_object_or_404
from .models import *
from word.models import *
from django.http import HttpResponse


# Create your views here.


def article_list(request):
        articles = Article.objects.all()
        return render(request, 'News/article_list.html', {'articles': articles})


def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'News/article_detail.html', {'article': article})


def article_voca(request, fk):
    print(fk)
    vocas = ArticleVoca.objects.filter(article_id=fk)
    return render(request, 'News/article_voca.html', {'vocas': vocas, 'article_id': fk})

'''
@csrf_exempt
def add_my_voca(request, slug):
    print(">>> add_my_voca")
'''


