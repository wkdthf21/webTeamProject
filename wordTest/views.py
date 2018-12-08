from django.shortcuts import render, reverse, HttpResponseRedirect, redirect
import random
from word.models import Word

# Create your views here.
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
        max_size = len(Word.objects.all()) -1
        word_num = random.randrange(0, max_size)
        word = Word.objects.get(word_id=word_num)
        numberIndex = getNumbers(word_num, max_size)
        numbers = []

        if not isAskSpell:
            question = word.word_spell

            for i in numberIndex:
                temp = Word.objects.get(word_id=i)
                numbers.append(temp.word_mean)

        else:
            question = word.word_mean

            for i in numberIndex:
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


def getNumbers(answer, max_size):
    list = []
    ran_num = random.randint(0, max_size)

    for i in range(4):
        while ran_num in list:
            ran_num = random.randint(0, max_size)
        if ran_num != answer:
            list.append(ran_num)
            i = i-1

    list.insert(random.randint(0, 3), answer)

    return list
