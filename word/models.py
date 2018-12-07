from django.db import models

# Create your models here.

class Word(models.Model):
    word_id=models.IntegerField()
    word_spell=models.CharField()
    word_mean=models.CharField()
    word_update_date=DateTimeField(default=timezone.now)
    u_id=ForeignKey('account.user', on_delete=models.CASCADE)
