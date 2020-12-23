from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    questions = Question.objects.all()
    context = {'questions': questions}
    context['title'] = 'Polls'
    return render(request, 'poll/index.html', context)

def details(request, id=None):
    context = {}
    context['title'] = 'Polls'
    return render(request, 'poll/poll_details.html', context)

def update_poll(request, id=None):
    context = {}
    context['title'] = 'Polls'
    return render(request, 'poll/poll_update.html', context)
