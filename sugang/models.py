from datetime import datetime

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=10)

    def __unicode__(self):
        return self.name


class Subject(models.Model):

    SUB_CHOICES = (
        ('토익','토익'),
        ('토스','토익 스피킹'),
        ('토플','토플'),
        ('텝스','텝스'),
        ('기초문법','기초문법'),
        ('회화청취','회화청취'),
        ('영작문','영작문')
    )
    LEVEL_CHOICES = (
        ('초급','초급'),
        ('중급','중급'),
        ('고급','고급'),
        ('공통','공통')
    )

    sub_categorize = models.CharField(max_length=10,
                                      choices=SUB_CHOICES,
                                      default='토익')
    sub_name = models.CharField(max_length=30)
    sub_code = models.CharField(max_length=10, null=False)
    i_name = models.CharField(max_length=10)
    i_code = models.CharField(max_length=10)
    total_lecture = models.IntegerField(default=0)
    lecture_level = models.CharField(max_length=10,
                                      choices=LEVEL_CHOICES,
                                      default='공통')
    book = models.CharField(max_length=20)

    def __unicode__(self):
        return self.sub_name

class Take(models.Model):
    username = models.CharField(max_length=10)
    #username = models.ForeignKey('User')
    sub_code = models.CharField(max_length=10, null=False)

    def __unicode__(self):
        return self.username
