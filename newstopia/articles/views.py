from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from articles.models import Article, Paragraph, Article_Likes, Paragraph_Likes, Tags, Article_Tags
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def index(request):
    class Articledata(object):
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

    class Paragraphdata(object):
        def __init__(self, **kwargs):
            self.__dict__.update(kwargs)

    articles = Article.objects.all().order_by('-pub_date')
    articlesData = []
    searchFound = []
    amountParagraphs=0

    if request.method == 'POST':
        if request.POST['searchString']:
            search = request.POST['searchString']
            searchFound = []
            articlesData = []

            for a in articles:
                articleData = Articledata(article = a,
                                          isAuthor = request.user.is_authenticated() and a.author == request.user,
                                          hasLiked = True,
                                          paragraphs = [],
                                          article_resize = False,
                                          singleParagraph = False,
                                          )
                #Test for authentication, if not disregard likes
                if request.user.is_authenticated():
                    try:
                        Article_Likes.objects.get(user=request.user.email,
                                                  article=a)
                    except ObjectDoesNotExist:
                        articleData.hasLiked = False
                paragraphs = Paragraph.objects.filter(article=a).order_by('-rating')[0:5]
                amountParagraphs = Paragraph.objects.filter(article=a).order_by('-rating')[0:5].count()
                if amountParagraphs == 1:
                    articleData.singleParagraph = True
                if amountParagraphs > 3:
                    articleData.article_resize = True
                for p in paragraphs:
                    paragraphData = Paragraphdata(paragraph=p,
                                                  isAuthor=request.user.is_authenticated() and p.author == request.user.email,
                                                  hasLiked=True)

                    #Test for authentication, if not disregard likes
                    if request.user.is_authenticated():
                        try:
                            Paragraph_Likes.objects.get(user=request.user.email,
                                                        paragraph=p)
                        except ObjectDoesNotExist:
                            paragraphData.hasLiked = False

                    articleData.paragraphs.append(paragraphData)
                articlesData.append(articleData)

            for a in articlesData:
                if search[0] == '#':
                    text = search.replace("#", "")
                    text = text.replace(" ", "")
                    articleTags = Article_Tags.objects.filter(article=a.article)
                    for at in articleTags:
                        if at.tag.name == text:
                            searchFound.append(a)
                if search.lower() in a.article.title.lower():
                    if a not in searchFound:
                        searchFound.append(a)
                for p in a.paragraphs:
                    if search.lower() in p.paragraph.text.lower():
                        if a not in searchFound:
                            searchFound.append(a)

            articlesData = []

    for a in articles:
        articleData = Articledata(article = a,
                isAuthor = request.user.is_authenticated() and a.author == request.user,
                hasLiked = True,
                paragraphs = [],
                article_resize = False,
                singleParagraph = False
                )
        #Test for authentication, if not disregard likes
        if request.user.is_authenticated():
            try:
                Article_Likes.objects.get(user=request.user.email,
                                          article=a)
            except ObjectDoesNotExist:
                articleData.hasLiked = False
        paragraphs = Paragraph.objects.filter(article=a).order_by('-rating')[0:5]
        amountParagraphs = Paragraph.objects.filter(article=a).order_by('-rating')[0:5].count()
        if amountParagraphs == 1:
            articleData.singleParagraph = True
        if amountParagraphs > 3:
            articleData.article_resize = True
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

    if searchFound:
                articlesData = searchFound

    return render(request, 'articles/index.html', {'authenticated': request.user.is_authenticated(), 'user': request.user, 'articlesData': articlesData})

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

    tags = Article_Tags.objects.filter(article=article)
    tagData = []
    for a in tags:
        tagData.append(a)

    if request.method == 'GET' or not request.user.is_authenticated():
        return render(request, 'articles/detail.html', {'articleData': articleData,
                                                    'tagData': tagData, 'authenticated': request.user.is_authenticated()})
    elif request.method == 'POST':
        return render_to_response('articles/detail.html', {'articleData': articleData,
                                                    'tagData': tagData, 'authenticated': request.user.is_authenticated()}, context_instance=RequestContext(request))


def create(request):
    if not request.user.is_authenticated():
        return render(request, 'articles/create.html', {'authenticated':request.user.is_authenticated()})


    valid = False
    if request.method == 'GET':
        valid = True
    if request.method == 'POST':
        if request.POST['title'] != "":
            valid = True
        if request.POST['body'] != "":
            valid = True
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
        tags = request.POST['tags']
        tagData = []
        if tags:
            tags = tags.replace(" ", "")
            tags = tags.split(',')
        for i in tags:
            count = Tags.objects.filter(name=i).count()
            if count == 0:
                tag = Tags(name=i)
                tag.save()
                articleTag = Article_Tags(article=article, tag=Tags.objects.get(name=i))
                articleTag.save()
                tagData.append(articleTag)
            else:
                articleTag = Article_Tags(article=article, tag=Tags.objects.get(name=i))
                articleTag.save()
                tagData.append(articleTag)

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
        #url = reverse('detail', args=article.pk)
        return HttpResponseRedirect('/articles/%i/' % article.pk)
        """return render_to_response('articles/detail.html', {'articleData': articleData,
                                                    'tagData': tagData, 'valid':valid, 'authenticated':request.user.is_authenticated()},
                                                    context_instance=RequestContext(request))"""
    else:
        return render(request, 'articles/create.html', {'valid':valid, 'authenticated':request.user.is_authenticated()})

def about(request):
    return render(request, 'articles/about.html')

def archive(request):
    return render(request, 'articles/archive.html')

def faq(request):
    return render(request, 'articles/faq.html')

#to test: multiple likes same article/paragraph
def vote(request):
    if request.method == 'POST':
        if request.user.is_authenticated():
            id = request.POST['id']
            type = request.POST['type']
            difference = int(request.POST['difference'])
            if type == "article":
                hasvoted = Article_Likes.objects.filter(user=request.user).filter(article=Article.objects.get(pk=id))
                vote = Article_Likes(user=request.user, article=Article.objects.get(pk=id))
                article = Article.objects.get(pk=id)
                if article and not hasvoted:
                    if difference > 0:
                        vote.save()
                        article.rating += 1
                        article.save()
                    else:
                        vote.save()
                        article.rating -= 1
                        article.save()
            elif type == "paragraph":
                hasvoted = Paragraph_Likes.objects.filter(user=request.user).filter(paragraph=Paragraph.objects.get(pk=id))
                vote = Paragraph_Likes(user=request.user, paragraph=Paragraph.objects.get(pk=id))
                paragraph = Paragraph.objects.get(pk=id)
                if paragraph and not hasvoted:
                    if difference > 0:
                        vote.save()
                        paragraph.rating += 1
                        paragraph.save()
                    else:
                        vote.save()
                        paragraph.rating -= 1
                        paragraph.save()
    return HttpResponse("voted")
"""
def vote(request):
    if request.method == 'POST':
        if request.user.is_authenticated():
            id = request.POST['id']
            type = request.POST['type']
            difference = request.POST['difference']
            if type == "article":
                vote = Article_Likes(user=request.user, article=Article.objects.get(pk=id))
                article = Article.objects.get(pk=id)
                if article:
                        vote.save()
                        article.rating += 1
                        article.save()
            elif type == "paragraph":
                vote = Paragraph_Likes(user=request.user, paragraph=Paragraph.objects.get(pk=id))
                paragraph = Paragraph.objects.get(pk=id)
                if paragraph:
                        vote.save()
                        paragraph.rating += 1
                        paragraph.save()
    return HttpResponse("voted")
"""