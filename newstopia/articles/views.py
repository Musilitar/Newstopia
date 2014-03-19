from django.shortcuts import render, render_to_response
from articles.models import Article
from datetime import datetime

def index(request):
    articles = Article.objects.all().order_by('-pub_date')
    return render(request, 'articles/index.html', {'articles': articles})

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'articles/detail.html', {'article': article})

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST' :
        article.body = request.POST['body']
        article.save()
        return render_to_response('articles/detail.html', {'article':article})
    else:
        return render(request, 'articles/edit.html', {'article': article})

def create(request):
    valid = True
    if request.method == 'POST' :
        if request.POST['title'] == "":
            valid = False
        if request.POST['body'] == "":
            valid = False
    if request.method == 'POST' and valid:
        article = Article(title=request.POST['title'], body=request.POST['body'], pub_date=datetime.now())
        article.save()
        return  render_to_response('articles/detail.html', {'article':article})
    else:
        return render(request, 'articles/create.html', {'valid':valid})
