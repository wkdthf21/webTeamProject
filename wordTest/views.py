from django.shortcuts import render, reverse, HttpResponseRedirect, redirect
from django.db.models import Max
from django.utils import timezone
from django.contrib.auth import get_user_model
from word.models import Word
from .models import Review, Test
import random
import ast

SPELL = 0
MEAN = 1

# Create your views here.
def test_main(request):
    if 'userId' in request.session :
        user = get_user_model()
        userId = request.session['userId']
        words = Word.objects.filter(u_id=user.objects.get(username=userId))
        maxQues = 5
        if len(words) < 5:
            maxQues = len(words)

        return render(request, 'wordTest/main.html', {'userId' : userId,
                                                      'quesNum': maxQues,})

    else:
        redirect_to = reverse('Login')
        return HttpResponseRedirect(redirect_to)

def word_test(request):
    if 'userId' in request.session :
        userId = request.session['userId']

        isAskSpell = questionType()
        questionWord = ""

        user = get_user_model()
        words = Word.objects.filter(u_id=user.objects.get(username=userId))
        quesIndexs = getQuestions(words)

        if isDataNotExist(quesIndexs):
            NotExistSavedWord()

        quesNum=0
        word = Word.objects.get(word_id=quesIndexs[quesNum])
        indexs = getRandomNumbers(Word.objects.all(), quesIndexs[quesNum])
        indexs.append(quesIndexs[quesNum])
        random.shuffle(indexs)
        numbers = []
        wrong = []
        correct = []

        for i in indexs:
            temp = Word.objects.get(word_id=i)
            numbers.append(temp)

            if request.method == 'POST':
                selector = request.POST['num']
                quesId = request.POST['quesId']
                quesNum = int(request.POST['quesNum'])
                wrong = ast.literal_eval(request.POST['wrong'])
                correct = ast.literal_eval(request.POST['correct'])

                if selector != quesId:
                    wrong.append(quesId)

                else:
                    correct.append(quesId)

                maxQues = 5
                if len(words) < 5:
                    maxQues = len(words)

                if quesNum == maxQues:
                    me = user.objects.get(username=userId)
                    score = int(len(correct)/maxQues * 100)
                    Test.objects.create(test_date=timezone.now(), u_id=me, score=score)

                    for wrong_word in set(wrong):
                        Review.objects.create(test_id =Test.objects.latest('pk'), wrong_word_id=Word.objects.get(word_id=wrong_word))

                    return render(request, 'result/result.html',
                                            {'userId': userId,
                                             'correct': len(correct),
                                             'wrong': len(wrong),
                                             'score': score,})

        return render(request, 'wordTest/test.html',
                                {'userId' : userId,
                                 'isAskSpell': isAskSpell,
                                 'questionNum': quesNum+1,
                                 'correct': correct,
                                 'wrong': wrong,
                                 'word': word,
                                 'numbers': numbers,})

    else:
        redirect_to = reverse('Login')
        return HttpResponseRedirect(redirect_to)


def getQuestions(words):
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

def questionType():
    return random.randrange(SPELL, MEAN)

def NotExistSavedWord():
    redirect_to = reverse('TestMain')
    return HttpResponseRedirect(redirect_to)

def isDataNotExist(data):
    return len(data)
