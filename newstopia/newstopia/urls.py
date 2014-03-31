from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^articles/', include('articles.urls', namespace="articles")),
    url(r'^account/', include('authentication.urls', namespace="account")),
    url(r'^tags/', include('tags.urls', namespace="tags")),
    url(r'^admin/', include(admin.site.urls)),
)
