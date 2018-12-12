from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.


def voca_main(request):
    return render(request, 'Vocabulary/voca_main.html')

