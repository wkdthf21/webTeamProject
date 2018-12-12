from django.shortcuts import render, reverse, HttpResponseRedirect, redirect
from django.db.models import Max
from django.contrib.auth import get_user_model
from word.models import Word
import random

SPELL = 0
MEAN = 1

# Create your views here.
def test_main(request):
    userId = isUserId(request)

    return render(request, 'wordTest/main.html', {'userId' : userId})


def word_test(request):
    userId = isUserId(request)

    isAskSpell = questionType()
    questionWord = ""

    quesIndexs = getQuestions()

    if isDataNotExist(quesIndexs):
        NotExistSavedWord()

    quesNum=0
    word = Word.objects.get(word_id=quesIndexs[quesNum])
    indexs = getRandomNumbers(Word.objects.all(), quesIndexs[quesNum])
    indexs.append(quesIndexs[quesNum])
    random.shuffle(indexs)
    numbers = []

    if not isAskSpell:
        questionWord = word.word_spell

        for i in indexs:
            temp = Word.objects.get(word_id=i)
            numbers.append(temp.word_mean)

    else:
        questionWord = word.word_mean

        for i in indexs:
            temp = Word.objects.get(word_id=i)
            numbers.append(temp.word_spell)

    return render(request, 'wordTest/test.html',
                                {'userId' : userId,
                                 'isAskSpell': isAskSpell,
                                 'questionNum': quesNum+1,
                                 'word': questionWord,
                                 'number1': numbers[0],
                                 'number2': numbers[1],
                                 'number3': numbers[2],
                                 'number4': numbers[3],
                                 'number5': numbers[4],
    })

def getQuestions():
    user = get_user_model()
    words = Word.objects.filter(u_id=user.objects.get(username='1111'))
    question_word_ids = []

    if len(words) < 4:
        for word in words:
            question_word_ids.append(word.word_id)
    else:
        question_word_ids = getRandomNumbers(words, " ")

    random.shuffle(question_word_ids)

    questions = {}
    for index, id in enumerate(question_word_ids):
        questions[index] = id

    return questions

def getRandomNumbers(AllObj, id):
    max_id = AllObj.aggregate(max_id=Max("word_id"))['max_id']
    result = []

    while True:
        word_id = random.randint(0, max_id)
        word = Word.objects.filter(word_id=word_id).first()
        if word and word.word_id not in result and word.word_id != id:
            result.append(word.word_id)
            if len(result) == 4:
                return result

def isUserId(request):
    if 'userId' in request.session :
        userId = request.session['userId']
        return userId

           # 로그인을 하지 않은 상태
    else:
        redirect_to = reverse('Login')
        return HttpResponseRedirect(redirect_to)

def questionType():
    return random.randrange(SPELL, MEAN)

def NotExistSavedWord():
    redirect_to = reverse('TestMain')
    return HttpResponseRedirect(redirect_to)

def isDataNotExist(data):
    return len(data)
