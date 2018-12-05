from django.shortcuts import render

# Create your views here.

# 비디오 메인 페이지 테스트
def Test_VideoMain(request):

    return render(request, 'TestVideoMain.html')

# /Video/list/
def VideoList(request):

    return render(request, 'VideoList.html')
