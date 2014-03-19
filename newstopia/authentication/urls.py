from django.conf.urls import patterns, include, url
from django.contrib import admin
from authentication import views

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', views.profile, name='profile'),
                       url(r'^login/$', views.acclogin, name='login'),
                       url(r'^register/$', views.registration, name='register'),
                       url(r'^logout/$', views.acclogout, name='logout'),
                       )