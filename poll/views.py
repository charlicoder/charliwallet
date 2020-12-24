from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
# Create your views here.

def index(request):
    questions = Question.objects.all()
    context = {'questions': questions}
    context['title'] = 'Polls'
    return render(request, 'poll/index.html', context)


def details(request, id=None):
    # obj = Question.objects.get(pk=id)
    obj = get_object_or_404(Question, id=id)
    context = {'question': obj}
    context['title'] = 'Polls'
    return render(request, 'poll/poll_details.html', context)


def poll_add(request):
    form = QuestionForm(request.POST or None)
    context = {}
    if request.method == 'POST':
        context['message'] = 'This is POST request'
    else:
        context['message'] = 'This is GET request'

    context['title'] = 'Add Poll'
    context['form'] = form

    return render(request, 'poll/poll_add.html', context)



def update_poll(request, id=None):
    context = {}
    context['title'] = 'Polls'
    return render(request, 'poll/poll_update.html', context)
