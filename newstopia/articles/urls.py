from django.conf.urls import patterns, include, url
from django.contrib import admin
from articles import views

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', views.IndexView.as_view(), name='index'),
                       url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
                       url(r'^new', views.NewView.as_view(), name='new'),
                       )


