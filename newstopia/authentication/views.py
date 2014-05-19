from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from authentication.models import Contributor
from articles.models import Paragraph, Paragraph_Likes, Article, Article_Likes


# Create your views here.

def registration(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('authentication/profile.html')
    if request.method == 'POST':
        user = Contributor(email=request.POST['username'], points=0)
        user.set_password(request.POST['password'])
        user.save()
        return HttpResponseRedirect('/account/')

    else:
        return render(request, 'authentication/register.html')


def acclogin(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/articles/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        contributor = authenticate(username=username, password=password)
        if contributor is not None:
            login(request, contributor)
            return HttpResponseRedirect('/articles/')
        else:
            return HttpResponseRedirect('/articles/')
    else:
        return render(request, 'authentication/login.html')


def profile(request):
    if request.user.is_authenticated():
        paragraphs = Paragraph.objects.filter(author=request.user.email)
        counterParagraphs = 0
        procentParagraphs = 0
        for p in paragraphs:
            counterParagraphs += 1
        paragraphLikes = Paragraph_Likes.objects.all()
        counterParagraphLikes = 0
        for l in paragraphLikes:
            for p in paragraphs:
                if l.paragraph == p:
                    counterParagraphLikes += 1
        articles = Article.objects.filter(author=request.user.email)
        counterArticles = 0
        for a in articles:
            counterArticles += 1
        articleLikes = Article_Likes.objects.all()
        counterArticleLikes = 0
        for l in articleLikes:
            for a in articles:
                if l.article == a:
                    counterArticleLikes += 1

        allParagraphs = Paragraph.objects.all()
        counterAllParagraphs = 0
        for a in allParagraphs:
            counterAllParagraphs += 1
        allUsers = Contributor.objects.all()
        counterAllUsers = 0
        for a in allUsers:
            counterAllUsers += 1
        averageParagraphs = 0
        if(counterAllParagraphs != 0 and counterAllUsers != 0):
            averageParagraphs = counterAllParagraphs / counterAllUsers
        averageParagraphLikes = 0
        if(counterParagraphLikes != 0 and counterAllParagraphs != 0):
            averageParagraphLikes = counterAllParagraphs / counterParagraphLikes
        allArticles = Article.objects.all()
        counterAllArticles = 0
        for a in allArticles:
            counterAllArticles += 1
        averageArticles = 0
        if(counterAllArticles != 0 and counterAllUsers != 0):
            averageArticles = counterAllArticles / counterAllUsers
        averageArticleLikes = 0
        if(counterArticleLikes != 0 and counterAllArticles != 0):
            averageArticleLikes = counterAllArticles / counterArticleLikes

        def calculateStars(procent):
            if procent > 80:
                return 5
            elif procent > 60:
                return 4
            elif procent > 40:
                return 3
            elif procent > 20:
                return 2
            else:
                return 1

        procentParagraphs = counterParagraphs / averageParagraphs * 100;
        starsParagraphs = calculateStars(procentParagraphs)
        procentParagraphLikes = counterParagraphLikes / averageParagraphLikes * 100;
        starsParagraphLikes = calculateStars(procentParagraphLikes)
        procentArticles = counterArticles / averageArticles * 100;
        starsArticles = calculateStars(procentArticles)
        procentArticleLikes = counterArticleLikes / averageArticleLikes * 100;
        starsArticleLikes = calculateStars(procentArticleLikes)


        return render_to_response('authentication/profile.html', {'numberOfParagraphs': counterParagraphs, 'numberOfParagraphLikes': counterParagraphLikes,
                                                                  'numberOfArticles': counterArticles, 'numberOfArticleLikes': counterArticleLikes,
                                                                  'averageParagraphs': averageParagraphs, 'averageParagraphLikes': averageParagraphLikes,
                                                                  'averageArticles': averageArticles, 'averageArticleLikes': averageArticleLikes,
                                                                  'starsParagraphs': range(starsParagraphs), 'starsParagraphLikes': range(starsParagraphLikes),
                                                                  'starsArticles': range(starsArticles), 'starsArticleLikes': range(starsArticleLikes)}, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/account/login/')


def acclogout(request):
    logout(request)
    return HttpResponseRedirect('/articles/')