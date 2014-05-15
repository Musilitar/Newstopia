from django.shortcuts import render, render_to_response
from django.template import RequestContext
from articles.models import Article, Paragraph, Article_Likes, Paragraph_Likes, Tags, Article_Tags
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist

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

    #if request.method == 'GET':
    #    articles = articles.filter(title__search=request.GET['searchString'])

    for a in articles:
        articleData = Articledata(article = a,
                isAuthor = request.user.is_authenticated() and a.author == request.user,
                hasLiked = True,
                paragraphs = [])
        #Test for authentication, if not disregard likes
        if request.user.is_authenticated():
            try:
                Article_Likes.objects.get(user=request.user.email,
                                          article=a)
            except ObjectDoesNotExist:
                articleData.hasLiked = False
        paragraphs = Paragraph.objects.filter(article=a).order_by('-rating')[0:5]
        for p in paragraphs:
            paragraphData = Paragraphdata(paragraph = p,
                                          isAuthor = request.user.is_authenticated() and p.author == request.user.email,
                                          hasLiked = True)

            #Test for authentication, if not disregard likes
            if request.user.is_authenticated():
                try:
                    Paragraph_Likes.objects.get(user=request.user.email,
                                                paragraph=p)
                except ObjectDoesNotExist:
                    paragraphData.hasLiked = False

            articleData.paragraphs.append(paragraphData)
        articlesData.append(articleData)
    tags = Tags.objects.all().order_by('name')
    return render(request, 'articles/index.html', {'authenticated': request.user.is_authenticated(), 'user': request.user, 'articlesData': articlesData, 'tags':tags})

def detail(request, pk):
    class Articledata(object):
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

    class Paragraphdata(object):
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

    if request.user.is_authenticated():
        if request.method == 'POST':
            if request.POST['new_paragraph']:
                p = Paragraph(article=Article.objects.get(pk=pk),
                              text=request.POST['new_paragraph'],
                              rating=0,
                              author=request.user,
                              pub_date=datetime.now())
                p.save()


    article = Article.objects.get(pk=pk)
    articleData = Articledata(article = article,
            isAuthor = request.user.is_authenticated() and article.author == request.user.email,
            hasLiked = True,
            paragraphs = [])

    if request.user.is_authenticated():
        try:
            Article_Likes.objects.get(user=request.user.email,
                                      article=article)
        except ObjectDoesNotExist:
            articleData.hasLiked = False
    paragraphs = Paragraph.objects.filter(article=article).order_by('-rating')
    for p in paragraphs:
        paragraphData = Paragraphdata(paragraph = p,
                                      isAuthor = request.user.is_authenticated() and p.author == request.user.email,
                                      hasLiked = True)
        if request.user.is_authenticated():
            try:
                Paragraph_Likes.objects.get(user=request.user.email,
                                            paragraph=p)
            except ObjectDoesNotExist:
                paragraphData.hasLiked = False

        articleData.paragraphs.append(paragraphData)

    tags = Tags.objects.all().order_by('name')
    if request.method == 'GET' or not request.user.is_authenticated():
        return render(request, 'articles/detail.html', {'articleData': articleData,
                                                    'tags': tags, 'authenticated': request.user.is_authenticated()})
    elif request.method == 'POST':
        return render_to_response('articles/detail.html', {'articleData': articleData,
                                                    'tags': tags, 'authenticated': request.user.is_authenticated()}, context_instance=RequestContext(request))


def create(request):
    valid = True
    if request.method == 'POST':
        if request.POST['title'] == "":
            valid = False
        if request.POST['body'] == "":
            valid = False
    if request.method == 'POST' and valid:

        class Articledata(object):
            def __init__(self, **kwargs):
                self.__dict__.update(kwargs)

        class Paragraphdata(object):
            def __init__(self, **kwargs):
                self.__dict__.update(kwargs)


        article = Article(title=request.POST['title'], pub_date=datetime.now(), author=request.user)
        article.save()
        paragraph = Paragraph(article=article, text=request.POST['body'], author=request.user, pub_date=datetime.now())
        paragraph.save()

        article = Article.objects.get(pk=article.pk)
        articleData = Articledata(article = article,
                isAuthor = article.author == request.user.email,
                hasLiked = True,
                paragraphs = [])
        try:
            Article_Likes.objects.get(user=request.user.email,
                                      article=article)
        except ObjectDoesNotExist:
            articleData.hasLiked = False
        paragraphs = Paragraph.objects.filter(article=article).order_by('-rating')
        for p in paragraphs:
            paragraphData = Paragraphdata(paragraph = p,
                                          isAuthor = p.author == request.user.email,
                                          hasLiked = True)
            try:
                Paragraph_Likes.objects.get(user=request.user.email,
                                            paragraph=p)
            except ObjectDoesNotExist:
                paragraphData.hasLiked = False

            articleData.paragraphs.append(paragraphData)

        tags = Tags.objects.all().order_by('name')


        return render_to_response('articles/detail.html', {'articleData': articleData,
                                                    'tags': tags}, context_instance=RequestContext(request))
    else:
        return render(request, 'articles/create.html', {'valid':valid})
