from django.db import models


class news(models.Model):
    title = models.CharField(max_length=500)
    url = models.CharField(max_length=500)
    date = models.IntegerField(default=12)
    month = models.CharField(max_length=50,default="june")
    year = models.IntegerField(default=2020)
    file = models.FileField(upload_to ='files/')
    has_url = models.BooleanField(default = True)
    has_file = models.BooleanField(default = True)