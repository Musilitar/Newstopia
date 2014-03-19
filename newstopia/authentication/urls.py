from django.conf.urls import patterns, include, url
from django.contrib import admin
from authentication import views

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', views.profile, name='index'),
                       url(r'^login/$', views.login, name='detail'),
                       url(r'^register/$', views.registration, name='edit'),
                       url(r'^logout/$', views.logout, name='create'),
                       )