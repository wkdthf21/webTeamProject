from django.db import models
from django.utils import timezone

# Create your models here.

class Word(models.Model):
    word_id=models.AutoField(primary_key=True)
    word_spell=models.CharField(max_length=20)
    word_mean=models.CharField(max_length=20)
    word_update_date = models.DateTimeField(default=timezone.now)
    #u_id = models.ForeignKey('account.user', on_delete=models.CASCADE)
    u_id = models.IntegerField()
