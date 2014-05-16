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
    rating = models.IntegerField(default=0)

    author = models.ForeignKey(Contributor)

class Paragraph(models.Model):
    def __str__(self):
        return self.text

    article = models.ForeignKey(Article)
    text = models.CharField(max_length=9999)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(Contributor, related_name="paragraph_authorset")
    pub_date = models.DateTimeField('date published')

class Paragraph_Likes(models.Model):
    user = models.ForeignKey(Contributor, related_name="paragraph_likes_userset")
    paragraph = models.ForeignKey(Paragraph, related_name="paragraph_likes_paragraphset")

class Article_Likes(models.Model):
    user = models.ForeignKey(Contributor, related_name="article_likes_userset")
    article = models.ForeignKey(Article, related_name="article_likes_articleset")

class Tags(models.Model):
    name = models.CharField(max_length=128)

class Article_Tags(models.Model):
    article = models.ForeignKey(Article)
    tag = models.ForeignKey(Tags)
    value = models.IntegerField(default=0)

