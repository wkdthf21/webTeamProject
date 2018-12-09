from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class video(models.Model):

    video_id = models.AutoField(primary_key=True)
    video_name = models.CharField(max_length = 100)
    video_url = models.CharField(max_length = 200)
    video_update_date =  models.DateTimeField(auto_now = True)
    u_id =  models.ForeignKey(User, on_delete=models.CASCADE)
