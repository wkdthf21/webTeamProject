from django.db.models.functions import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth.models import User

from .forms import ClassForm
from .forms import TakeForm
from .models import Take, Subject


def SugangMain(request):
    subjects = Subject.objects.all()
    context = {'subjects' : subjects}
    template_name='sugang/SugangMain.html'

    if request.method=="POST":
        subject_id = request.POST['sign']
        subject = Subject.objects.get(pk=subject_id)
        #수강 이미 존재 하는지 확인
        if Take.objects.filter(username=request.user, sub_code=subject.sub_code).exists():
            return HttpResponse('이미 수강 신청한 과목입니다.')
        else:
            sign = Take(username=request.user, sub_code=subject.sub_code)
            sign.save()
        return HttpResponse('수강 신청 완료')
    else:
        return render(request, template_name, context)


def thanks(request):
    template_name='sugang/thanks.htmㅣ'
    return render(request,template_name)

def myclass(request):
    template_name='sugang/myclass.html'
    subjects = Subject.objects.all()
    takes = Take.objects.all()
    context = {'takes': takes, 'subjects':subjects}

    return render(request, template_name, context)


def SugangAddNewClass(request):
    template_name='sugang/SugangAddNewClass.html'
    model = Subject
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            new_class = form.save(commit=False)
            new_class.save()
            return redirect('thanks')
    else:
        form = ClassForm()
    return render(request, template_name, {'form': form})
