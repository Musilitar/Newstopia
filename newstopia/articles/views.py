from django.shortcuts import render, render_to_response
from articles.models import Article, ArticleVersion
from datetime import datetime

# IN COMMENTAAR HOPELIJK NIEUWE MANIER VAN WERKEN MET ARTIKELS

def index(request):
    articles = Article.objects.all().order_by('-pub_date')
    #for article in articles:
        #if article.version != 1:
            #article_version = ArticleVersion.objects.get(pk=article.version)
            #article.body = article_version.changed_text
    return render(request, 'articles/index.html', {'articles': articles})

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    #article_version = ArticleVersion.objects.get(pk=article.version)
    #article.body = article_version.changed_text
    return render(request, 'articles/detail.html', {'article': article})

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.body = request.POST['body']
        article.save()
        #article_version = ArticleVersion(article_id=article.pk, changed_text=request.POST['body'])
        #article_version.save()
        #article.version = article_version.pk
        #article.save()
        return render_to_response('articles/detail.html', {'article':article})
    else:
        #if article.version != 1:
            #article_version = ArticleVersion.objects.get(pk=article.version)
            #article.body = article_version.changed_text
        return render(request, 'articles/edit.html', {'article': article})

def create(request):
    valid = True
    if request.method == 'POST':
        if request.POST['title'] == "":
            valid = False
        if request.POST['body'] == "":
            valid = False
    if request.method == 'POST' and valid:
        article = Article(title=request.POST['title'], body=request.POST['body'], pub_date=datetime.now())#, version=1)
        article.save()
        #article_version = ArticleVersion(article_id=article.pk, changed_text=request.POST['body'], base=True)
        #article_version.save()
        return  render_to_response('articles/detail.html', {'article':article})
    else:
        return render(request, 'articles/create.html', {'valid':valid})
