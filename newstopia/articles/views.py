from django.shortcuts import render, render_to_response
from articles.models import Article, Paragraph
from datetime import datetime

def index(request):
    articles = Article.objects.all().order_by('-pub_date')
    paragraphs = Paragraph.objects.all()
    for article in articles:
        paragraphs = Paragraph.objects.all().filter(article_id=article.pk)
        highest_rated = Paragraph()
        highest_rated2 = Paragraph()
        for paragraph in paragraphs:
            if paragraph.rating >= highest_rated.rating:
                highest_rated = paragraph
            elif paragraph.rating >= highest_rated2.rating:
                highest_rated2 = paragraph
        paragraphs = {highest_rated, highest_rated2}
    return render(request, 'articles/index.html', {'articles': articles, 'paragraphs': paragraphs})

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    paragraphs = Paragraph.objects.filter(article=pk)
    if request.method == 'POST':
        p = Paragraph(text=request.POST['new_paragraph'], article=article, rating=0)
        p.save()
        return render_to_response('articles/detail.html', {'article': article,
                                                            'paragraphs': paragraphs})
    else:
        return render(request, 'articles/detail.html', {'article': article,
                                                    'paragraphs': paragraphs})

"""def edit(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article_version = ArticleVersion(article=article, changed_text=request.POST['body'])
        article_version.save()
        article.version += 1
        article.pub_date = datetime.now()
        article.save()
        article.body = article_version.changed_text
        return render_to_response('articles/detail.html', {'article':article})
    else:
        if article.version != 1:
            article_version = ArticleVersion.objects.get(pk=article.version)
            article.body = article_version.changed_text
        return render(request, 'articles/edit.html', {'article': article})"""

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
        return  render_to_response('articles/detail.html', {'article':article})
    else:
        return render(request, 'articles/create.html', {'valid':valid})
