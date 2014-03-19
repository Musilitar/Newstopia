import datetime
from django.db import models
from django.forms import ModelForm
from django.utils import timezone

class Article(models.Model):
    def __str__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.CharField(max_length=9999)
