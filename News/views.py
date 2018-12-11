from django.shortcuts import render
from django.http import HttpResponse

#from .models import Article

# Create your views here.


def post_list(request):
    return render(request, 'News/post_list.html', {})

'''
def show_article(request):
    article = Article.objects.all()
    context = {'article': article}
    return render(request, 'News/article.html', context)
'''