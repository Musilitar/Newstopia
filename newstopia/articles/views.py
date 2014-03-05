from django.views import generic
from django.core.urlresolvers import reverse
from articles.models import Article, ArticleForm


class IndexView(generic.ListView):
    template_name = 'articles/index.html'
    context_object_name = 'all_articles'

    def get_queryset(self):
        return Article.objects.order_by('-pub_date')


class DetailView(generic.DetailView):
    model = Article
    template_name = 'articles/detail.html'


class NewView(generic.CreateView):
    model = Article
    template_name = 'articles/create.html'
    success_url = '/articles/'


class EditView(generic.UpdateView):
    model = Article
    fields = ['title', 'body']
    template_name = 'articles/edit.html'
    success_url = '../'


