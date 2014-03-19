from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from customers.forms import RegistrationForm
from customers.forms import LoginForm
from authentication.models import Contributor


# Create your views here.

def registration(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/contributor/')
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = Contributor.objects.create_user(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            return HttpResponseRedirect('/contributor/')
        else:
            return render_to_response('register.html', {'form': form}, context_instance=RequestContext(request))

    else:
        form = RegistrationForm()
        context = {'form': form}
        return render_to_response('register.html', context, context_instance=RequestContext(request))


def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/contributor/')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            contributor = authenticate(username=username, password=password)
            if contributor is not None:
                login(request, contributor)
                return HttpResponseRedirect('/contributor/')
            else:
                return HttpResponseRedirect('/contributor/login/')
        else:
            return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))

    else:
        form = LoginForm()
        context = {'form': form}
        return render_to_response('login.html', context, context_instance=RequestContext(request))


def profile(request):
    if request.user.is_authenticated():
        return render_to_response('profile.html', None, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/contributor/login/')


def logout(request):
    logout(request)
    return HttpResponseRedirect('/contributor/login/')