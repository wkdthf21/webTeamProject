from django.db import models
from django.utils import timezone

# Create your models here.

class Test(models.Model):
    test_id = models.IntegerField()
    test_date = models.DateTimeField(default=timezone.now)
#    u_id = models.ForeignKey('account.user', on_delete=models.CASCADE) 
    u_id = models.IntegerField()
    score = models.IntegerField()


class Review(models.Model):
    test_id = models.ForeignKey('wordTest.Test', on_delete=models.CASCADE)
#    wrong_word_id = models.ForeignKey('word.Word', on_delete=models.CASCADE)
    wrong_word_id = models.IntegerField()
