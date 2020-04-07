from django.shortcuts import render

from .models import Question, Choices

# get question and display
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list':latest_question_list}
    return render(request, 'polls/index.html', context)

#specific question and  choices
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("qustion does'nt exist")
    return render(request, 'polls/results.html', {'question': question})