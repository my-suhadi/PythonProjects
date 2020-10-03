from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView

from .models import Question, Choice


# Create your views here.

class IndexView(ListView):
    # The automatically generated context variable is question_list.
    # To override this we provide the context_object_name
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailPollsView(DetailView):
    # By default, the DetailView generic view uses a template called <app name>/<model name>_detail.html
    model = Question
    template_name = 'polls/detail.html'


class ResultView(DetailView):
    # Context dibuat otomatis sesuai nama model
    model = Question
    template_name = 'polls/result.html'


def vote(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = q.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question_key': q,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:result', args=(question_id,)))
