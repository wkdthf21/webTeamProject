from django.db.models.functions import datetime
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth.models import User

from .forms import ClassForm, SignForm
from .forms import TakeForm
from .models import Take, Subject, Instructor


def SugangMain(request):
    # 수강 신청 메인
    template_name='sugang/SugangMain.html'
    # 전체 과목, 전체 교사, 사용자 정보
    subjects = Subject.objects.all()
    instructors = Instructor.objects.all()
    user = User.objects.get(id=request.user.id)

    if Instructor.objects.filter(i_id=user.id).exists():
        #사용자가 교사라면 교사 정보 포함
        instructor = Instructor.objects.get(i_id=user.id)
        context = {'subjects': subjects, 'user': user, 'instructors':instructors,'instructor': instructor}
        return render(request, template_name, context)
    else:
        instructor = None
        context = {'subjects': subjects, 'user': user, 'instructors':instructors,'instructor': instructor}
        if request.method == "POST":
            subject_id = request.POST['sign']
            subject = Subject.objects.get(pk=subject_id)
            # 수강 기록 존재 여부 확인
            if Take.objects.filter(username_id=user.id, subject_id=subject.id).exists():
                return HttpResponse('이미 수강 신청한 과목입니다.')
            else:
                sign = Take(username_id=user.id, subject_id=subject.id)
                sign.save()
            return HttpResponse('수강 신청 완료')
        else:
            return render(request, template_name, context)



def thanks(request):
    template_name='sugang/Thanks.html'
    return render(request,template_name)

def delete(request,take_id):
    template_name = 'sugang/delete.html'
    take = Take.objects.get(pk=take_id)

    if request.method == 'POST':
        take.delete();
        return render(request, template_name)
    else:
        return render(request, template_name)

def myclass(request):
    template_name='sugang/Myclass.html'
    user = User.objects.get(id=request.user.id)
    subjects = Subject.objects.all()
    takes = Take.objects.all()

    # 교사와 일반 사용자 구분
    if Instructor.objects.filter(i_id=user.id).exists():
        instructor = Instructor.objects.get(i_id=user.id)
        context = {'takes': takes,'subjects': subjects, 'user': user,'instructor': instructor}
    else:
        instructor = None
        context = {'takes': takes, 'subjects':subjects, 'user':user,'instructor': instructor}

    return render(request, template_name, context)


def SugangAddNewClass(request):
    # 새 강의 개설 - 사용자가 교사일 때 수강신청 메인 화면에서 접근 가능
    template_name='sugang/SugangAddNewClass.html'
    users = User.objects.all()
    user = User.objects.get(id=request.user.id)
    instructor = Instructor.objects.get(i_id=user.id)

    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            new_class = form.save(commit=False)
            new_class.save()
            return redirect('Thanks')
    else:
        form = ClassForm(initial={'i_name': instructor.id})
    context = {'users':users, 'instructor':instructor,'form': form}

    return render(request, template_name, context)



def SignInstructor(request):
    template_name = 'sugang/SignInstructor.html'
    #instructors = Instructor.objects.all()
    user = User.objects.get(username=request.user)

    if request.method == 'POST':
        if Instructor.objects.filter(i_id=user.id).exists():
            return HttpResponse('이미 강사로 전환된 회원입니다.')
        else:
            form = SignForm(request.POST)
            if form.is_valid():
                # id는 form에서 initial set
                # 비밀번호 확인
                password = form.cleaned_data['i_pw']

                if user.check_password(password):
                    new_sign = form.save(commit=False)
                    new_sign.save()
                    return HttpResponse('강사 전환 완료')
                else :
                    raise forms.ValidationError("wrong password")

    else:
        # not POST initial set
        form = SignForm(initial={'i_id': user.id})
    context = {'form': form,'user':user}
    return render(request, template_name,context)
