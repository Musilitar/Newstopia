import datetime
from django.db import models
from django.utils import timezone
from authentication.models import Contributor

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
    version = models.IntegerField(default=1)

class Paragraph(models.Model):
    def __str__(self):
        return self.text

    article = models.ForeignKey(Article)
    text = models.CharField(max_length=9999)
    rating = models.IntegerField(default=0)

class UserParagraph(models.Model):
    user = models.ForeignKey(Contributor)
    paragraph = models.ForeignKey(Paragraph)