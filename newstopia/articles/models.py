import datetime
from django.db import models
from django.utils import timezone

# IN COMMENTAAR HOPELIJK NIEUWE MANIER VAN WERKEN MET ARTIKELS

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
    #version = models.ForeignKey(ArticleVersion.pk)

"""class ArticleVersion(models.Model):
    def __str__(self):
        return self.changed_text

    article_id = models.ForeignKey(Article.pk)
    changed_text = models.CharField(max_length=9999)
    rating = models.IntegerField(default=0)
    base = models.BooleanField(default=False)"""
