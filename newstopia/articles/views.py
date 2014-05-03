from django.shortcuts import render, render_to_response
from django.template import RequestContext
from articles.models import Article, Paragraph
from datetime import datetime

"""
testcommit
"""

def index(request):
    articles = Article.objects.all().order_by('-pub_date')
    artpars = []
    class Artpar:
        article = Article()
        paragraphs = []
    for article in articles:
        artpar = Artpar()
        artpar.article = article
        artpar.paragraphs = Paragraph.objects.filter(article=article.pk).order_by('-rating')[0:2]
        artpars.append(artpar)
    return render_to_response('articles/index.html', {'artpars': artpars}, context_instance=RequestContext(request))

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    paragraphs = Paragraph.objects.filter(article=pk).order_by('-rating')
    if request.method == 'POST':
        if 'score' in request.POST:
            paragraph = Paragraph.objects.get(pk=request.POST['paragraph'])
            if request.POST['score'] == 'good':
                paragraph.rating += 1
                paragraph.save()
            elif request.POST['score'] == 'bad':
                paragraph.rating -= 1
                paragraph.save()
        else:
            p = Paragraph(text=request.POST['new_paragraph'], article=article, rating=0)
            p.save()
        return render_to_response('articles/detail.html', {'article': article,
                                                            'paragraphs': paragraphs}, context_instance=RequestContext(request))
    else:
        return render(request, 'articles/detail.html', {'article': article,
                                                    'paragraphs': paragraphs})

def create(request):
    valid = True
    if request.method == 'POST':
        if request.POST['title'] == "":
            valid = False
        if request.POST['body'] == "":
            valid = False
    if request.method == 'POST' and valid:
        article = Article(title=request.POST['title'], pub_date=datetime.now())
        article.save()
        paragraph = Paragraph(article=article, text=request.POST['body'])
        paragraph.save()
        return render_to_response('articles/detail.html', {'article':article})
    else:
        return render(request, 'articles/create.html', {'valid':valid})
