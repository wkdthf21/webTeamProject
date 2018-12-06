from django.shortcuts import render

# Create your views here.
def word_test(request):
    return render(request, 'wordTest/test.html', {})
