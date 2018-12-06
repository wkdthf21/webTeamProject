from django.shortcuts import render, reverse, HttpResponseRedirect, redirect

# Create your views here.

# 비디오 메인 페이지 테스트
def Test_VideoMain(request):

    return render(request, 'TestVideoMain.html')

# /Video/list/
def VideoList(request):

    # 로그인 했을 경우
    if 'userId' in request.session :
        userId = request.session['userId']
        return render(request, 'VideoList.html', {'userId' : userId})

    # 로그인 안했을 경우
    else:
        redirect_to = reverse('Main')
        return HttpResponseRedirect(redirect_to)
