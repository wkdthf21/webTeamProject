from django.shortcuts import render
from sugang.models import Take, Subject, Instructor
from django.contrib.auth.models import User

# Create your views here.

def Classroom(request,subject_id):
    template_name='classroom.html'
    subject = Subject.objects.get(pk = subject_id)
    user = User.objects.get(id=request.user.id)
    #take = Take.objects.filter(username_id=user.id, subject_id=subject.id).exists()
    instructor = Instructor.objects.get(id = subject.i_name.id)

    # 교사와 일반 사용자 구분
    if instructor.i_id.id == user.id:
        #사용자가 해당 과목 강사 일 때 # 글쓰기 기능 활성화
        instructor = Instructor.objects.get(i_id=user.id)
        context = {'subject': subject, 'user': user,'instructor': instructor}
    else :
        instructor = None
        context = {'subject':subject, 'user':user,'instructor': instructor}
    return render(request, template_name, context)

