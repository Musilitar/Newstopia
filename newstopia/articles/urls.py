from django.conf.urls import patterns, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from articles import views

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^(?P<pk>\d+)/$', views.detail, name='detail'),
                       url(r'^add/$', views.create, name='create'),
                       url(r'^about/$', views.about, name='about'),
                       ) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()
