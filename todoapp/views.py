from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404

from .models import Task, Hashtag

# Create your views here.


def index(request):
    unordered_task_list = Task.objects.all()
    ordered_task_list = sorted(unordered_task_list, reverse=True)
    context = {'task_list': ordered_task_list}
    return render(request, 'todoapp/index.html', context)


def task_detail(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        raise Http404("Task does not exists :(")
    return render(request, 'todoapp/task_detail.html', {'task': task})


def hashtag_detail(request, hashtag_id):
    hashtag = get_object_or_404(Hashtag, id=hashtag_id)
    tasks_in_which_used = hashtag.task_set.all()
    context = {'hashtag': hashtag, 'tasks_in_which_used': tasks_in_which_used}
    return render(request, 'todoapp/hashtag_detail.html',
                  context)
