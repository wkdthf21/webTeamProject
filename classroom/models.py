from django.db import models
from sugang.models import Take, Subject, Instructor
import os
from django.conf import settings

from django.core.files.storage import FileSystemStorage
# Create your models here.
class Board(models.Model):
    subject = models.ForeignKey('sugang.Subject',on_delete=models.CASCADE, default=0)
    title = models.CharField(verbose_name=u'제목', blank=True, max_length=256)
    content = models.TextField(u'내용', blank=True, default='')
    file = models.FileField(u'파일첨부',null=True, blank=True, upload_to="uploads/")
    #created = models.DateTimeField(auto_now_add=True, verbose_name=u'생성일')
    #upload_date = models.DateTimeField('Upload Date', auto_now_add=True)

    def __unicode__(self):
        return self.title