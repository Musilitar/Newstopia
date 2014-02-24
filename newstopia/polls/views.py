from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from django.views import generic
from polls.models import Choice, Poll


class IndexView(generic.ListView):
    template_name = 'articles/index.html'
    context_object_name = 'latest_poll_list'

    def get_queryset(self):
        """Return the last five published articles."""
        return Poll.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Poll
    template_name = 'articles/detail.html'


class ResultsView(generic.DetailView):
    model = Poll
    template_name = 'articles/results.html'


def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'articles/detail.html', {'poll': p, 'error_message': "No selection"})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('articles:results', args=(p.id,)))