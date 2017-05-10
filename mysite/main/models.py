import datetime
from django.utils import timezone
# Create your models here.
from django.db import models

class People(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    bio = models.CharField(max_length=2000)
    pub_date = models.DateTimeField('date published')
    pic_link = models.CharField(max_length=100)
    category = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

