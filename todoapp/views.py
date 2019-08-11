from django.shortcuts import render

from .models import Task, Hashtag

# Create your views here.


def index(request):
    task_list = Task.objects.all()
    context = {'task_list': task_list}
    return render(request, 'todoapp/index.html', context)


def task_detail(request, task_id):
    pass


def hashtag_detail(request, hashtag_id):
    pass
