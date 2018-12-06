from django.shortcuts import render, reverse, HttpResponseRedirect, redirect

# Create your views here.

def Main(request):

    # 로그인을 한 상태
    if 'userId' in request.session :
        userId = request.session['userId']
        return render(request, 'main.html', {'userId' : userId})

   # 로그인을 하지 않은 상태
    else:
        redirect_to = reverse('Login')
        return HttpResponseRedirect(redirect_to)
