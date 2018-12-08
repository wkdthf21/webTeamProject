from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Test(models.Model):
    #test_id = models.IntegerField(primary_key=True)
    test_date = models.DateTimeField(default=timezone.now)
    u_id = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()


class Review(models.Model):
    test_id = models.ForeignKey(Test, on_delete=models.CASCADE)
    wrong_word_id = models.ForeignKey('word.Word', on_delete=models.CASCADE)
