from django.shortcuts import render, reverse, HttpResponseRedirect, redirect

# Create your views here.

# 메인 화면 view
def Main(request):
    print('1')

    # 로그인을 한 상태
    if 'userId' in request.session :
        userId = request.session['userId']
        print('2')
        
        # 로그아웃 요청
        if request.method == "POST":

            mode = request.POST['Sign']
            print('3')

            if mode == '로그아웃':
                redirect_to = reverse('Logout')
                return HttpResponseRedirect(redirect_to)

        return render(request, 'main.html', {'userId' : userId})

   # 로그인을 하지 않은 상태
    else:
        redirect_to = reverse('Login')
        return HttpResponseRedirect(redirect_to)
