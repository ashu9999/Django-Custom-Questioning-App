from django.shortcuts import render

from .models import Question, Choices

# get question and display
def index(request):
    return render(request, 'polls/index.html')