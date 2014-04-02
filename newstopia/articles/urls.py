from django.conf.urls import patterns, include, url
from django.contrib import admin
from articles import views

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^(?P<pk>\d+)/$', views.detail, name='detail'),
                       url(r'^add/$', views.create, name='create'),

                       """url(r'^(?P<pk>\d+)/edit/$', views.edit, name='edit'),"""
                       )


