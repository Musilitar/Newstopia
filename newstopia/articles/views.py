from django.shortcuts import render, render_to_response
from django.template import RequestContext
from articles.models import Article, Paragraph, Article_Likes, Paragraph_Likes, Tags, Article_Tags
from datetime import datetime

"""
testcommit
"""

def index(request):
    class Articledata(object):
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

    class Paragraphdata(object):
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

    articles = Article.objects.all().order_by('-pub_date')
    articlesData = []
    for a in articles:
        articleData = Articledata(article = a,
                isAuthor = a.author == request.user.email,
                hasLiked = True,
                paragraphs = [])
        try:
            Article_Likes.objects.get(user=request.user.email,
                                      article=a)
        except Article_Likes.Doesnotexist:
            articleData.hasLiked = False
        paragraphs = Paragraph.objects.all(article=a.pk).order_by('-rating')[0:5]
        for p in paragraphs:
            paragraphData = Paragraphdata(paragraph = p,
                                          isAuthor = p.author == request.user.email,
                                          hasLiked = True)
            try:
                Paragraph_Likes.objects.get(user=request.user.email,
                                            paragraph=p)
            except Article_Likes.Doesnotexist:
                paragraphData.hasLiked = False

            articleData.paragraphs.append(paragraphData)
        articlesData.append(articleData)
    tags = Tags.objecs.all().order_by('name')
    return render_to_response('articles/index.html', {'user': request.user, 'articlesData': articlesData, 'tags':tags}, context_instance=RequestContext(request))

def detail(request, pk):
    class Articledata(object):
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

    class Paragraphdata(object):
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)
    article = Article.objects.get(pk=pk)
    articleData = Articledata(article = article,
            isAuthor = article.author == request.user.email,
            hasLiked = True,
            paragraphs = [])
    try:
        Article_Likes.objects.get(user=request.user.email,
                                  article=article)
    except Article_Likes.Doesnotexist:
        articleData.hasLiked = False
    paragraphs = Paragraph.objects.all(article=article.pk).order_by('-rating')
    for p in paragraphs:
        paragraphData = Paragraphdata(paragraph = p,
                                      isAuthor = p.author == request.user.email,
                                      hasLiked = True)
        try:
            Paragraph_Likes.objects.get(user=request.user.email,
                                        paragraph=p)
        except Article_Likes.Doesnotexist:
            paragraphData.hasLiked = False

        articleData.paragraphs.append(paragraphData)

    tags = Tags.objecs.all().order_by('name')

    render(request, 'articles/detail.html', {'articleData': articleData,
                                                    'tags': tags})

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
