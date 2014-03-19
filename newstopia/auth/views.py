from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from customers.forms import RegistrationForm
from customers.forms import LoginForm
from customers.models import Customer


# Create your views here.

def CustomerRegistration(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/customer/')
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'], email=form.cleaned_data['email'], password=form.cleaned_data['password'], first_name=form.cleaned_data['first_name'], last_name=form.cleaned_data['last_name'])
            return HttpResponseRedirect('/customer/')
        else:
            return render_to_response('register.html', {'form': form}, context_instance=RequestContext(request))

    else:
        form = RegistrationForm()
        context = {'form': form}
        return render_to_response('register.html', context, context_instance=RequestContext(request))

def CustomerLogin(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/customer/')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            customer = authenticate(username = username, password = password)
            if customer is not None:
                login(request, customer)
                return HttpResponseRedirect('/customer/')
            else:
                return HttpResponseRedirect('/customer/login/')
        else:
            return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request))

    else:
        form = LoginForm()
        context = {'form': form}
        return render_to_response('login.html', context, context_instance=RequestContext(request))

def CustomerProfile(request):
    if request.user.is_authenticated():
        return render_to_response('profile.html', None, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/customer/login/')

def CustomerLogout(request):
    logout(request)
    return HttpResponseRedirect('/customer/login/')from django.shortcuts import render

# Create your views here.
