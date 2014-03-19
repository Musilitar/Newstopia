from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from authentication.models import Contributor


# Create your views here.

def registration(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('authentication/profile.html')
    if request.method == 'POST':
        user = Contributor(email=request.POST['username'])
        user.set_password(request.POST['password'])
        user.save()
        return HttpResponseRedirect('/account/')

    else:
        return render(request, 'authentication/register.html')


def acclogin(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/account/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        contributor = authenticate(username=username, password=password)
        if contributor is not None:
            login(request, contributor)
            return HttpResponseRedirect('/account/')
        else:
            return HttpResponseRedirect('/account/login/')
    else:
        return render(request, 'authentication/login.html')


def profile(request):
    if request.user.is_authenticated():
        return render_to_response('authentication/profile.html', None, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/account/login/')


def acclogout(request):
    logout(request)
    return HttpResponseRedirect('/account/login/')