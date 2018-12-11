from django.shortcuts import render, reverse, HttpResponseRedirect, redirect
from django.db.models import Max
from word.models import Word
import random

# Create your views here.
def test_main(request):
    if 'userId' in request.session :
        userId = request.session['userId']

        # 로그아웃 요청
        if request.method == "POST":
            mode = request.POST['Sign']

            if mode == '로그아웃':
                redirect_to = reverse('Logout')
                return HttpResponseRedirect(redirect_to)

        return render(request, 'wordTest/main.html', {'userId' : userId})

       # 로그인을 하지 않은 상태
    else:
        redirect_to = reverse('Login')
        return HttpResponseRedirect(redirect_to)

def word_test(request):
    if 'userId' in request.session :
        userId = request.session['userId']

        # 로그아웃 요청
        if request.method == "POST":
            mode = request.POST['Sign']

            if mode == '로그아웃':
                redirect_to = reverse('Logout')
                return HttpResponseRedirect(redirect_to)

        isAskSpell = random.randrange(0, 1)
        questionNum = 0
        question = ""
        data = Word.objects.order_by('-pk')[0]
        # TODO data가 없을경우 예외처리
        indexs = getRandomQuestion(data.word_id)
        indexs.append(data.word_id)
        random.shuffle(indexs)
        numbers = []

        if not isAskSpell:
            question = data.word_spell

            for i in indexs:
                temp = Word.objects.get(word_id=i)
                numbers.append(temp.word_mean)

        else:
            question = data.word_mean

            for i in indexs:
                temp = Word.objects.get(word_id=i)
                numbers.append(temp.word_spell)

        return render(request, 'wordTest/test.html',
                                        {'userId' : userId,
                                         'isAskSpell': isAskSpell,
                                         'questionNum': questionNum+1,
                                         'word': question,
                                         'number1': numbers[0],
                                         'number2': numbers[1],
                                         'number3': numbers[2],
                                         'number4': numbers[3],
                                         'number5': numbers[4],
        })

   # 로그인을 하지 않은 상태
    else:
        redirect_to = reverse('Login')
        return HttpResponseRedirect(redirect_to)


def getRandomQuestion(id):
    max_id = Word.objects.all().aggregate(max_id=Max("word_id"))['max_id']
    result = []

    while True:
        word_id = random.randint(0, max_id)
        word = Word.objects.filter(word_id=word_id).first()
        if word and word.word_id not in result and word.word_id != id:
            result.append(word.word_id)
            if len(result) == 4:
                return result
