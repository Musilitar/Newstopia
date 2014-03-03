from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib import messages
from articles.models import Article, ArticleForm


class IndexView(generic.ListView):
    template_name = 'articles/index.html'
    context_object_name = 'latest_articles'

    def get_queryset(self):
        """Return the last five published articles."""
        return Article.objects.order_by('-pub_date')[:20]


class DetailView(generic.DetailView):
    model = Article
    template_name = 'articles/detail.html'


class NewView(generic.CreateView):
    model = Article
    template_name = 'articles/create.html'
    success_url = '/articles/'


def new(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return HttpResponseRedirect('/articles/')
    else:
        form = ArticleForm()
    return render_to_response('articles/index.html', {'form': form},)


def get(request, article_id):
    if request.method == 'POST':
        a = Article.objects.get(pk=article_id)
        f = ArticleForm(request.POST, instance=a)

class EditView(generic.CreateView):
    model = Article
    template_name = 'articles/edit.html'
    success_url = 'articles/'

def edit(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return HttpResponseRedirect('/articles/' + article.pk)
    else:
        form = ArticleForm()
    return render_to_response('articles/index.html', {'form': form},)#later naar artikel