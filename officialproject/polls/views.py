from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from .models import Question


# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        'latest_question_list_key': latest_question_list,
    }
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # try:
    #     q = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Object not found")

    q = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question_key': q})


def result(request, question_id):
    rs = "Result pertanyaan %s."
    return HttpResponse(rs % question_id)


def vote(request, question_id):
    return HttpResponse("Vote pertanyaan %s." % question_id)
