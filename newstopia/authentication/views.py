from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from authentication.models import Contributor
from articles.models import Paragraph, Paragraph_Likes


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
        for p in paragraphs:
            counterParagraphs += 1
        likes = Paragraph_Likes.objects.all()
        counterParagraphLikes = 0
        for l in likes:
            for p in paragraphs:
                if l.paragraph == p:
                    counterParagraphLikes += 1
        return render_to_response('authentication/profile.html', {'numberOfParagraphs': counterParagraphs, 'numberOfParagraphLikes': counterParagraphLikes}, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/account/login/')


def acclogout(request):
    logout(request)
    return HttpResponseRedirect('/articles/')