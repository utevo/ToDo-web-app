from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404

from .models import Task, Hashtag
from .forms import TaskForm, HashtagForm


def index(request):
    return HttpResponseRedirect(reverse('todoapp:tasks'))


def tasks(request):
    if request.method == 'GET':
        unordered_tasks = Task.objects.all()
        tasks = sorted(unordered_tasks, reverse=True)
        context = {'tasks': tasks}
        return render(request, 'todoapp/tasks.html', context)

    if request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            new_task = form.save(commit=True)
            return HttpResponseRedirect(reverse('todoapp:tasks'))


def hashtags(request):
    hashtags = Hashtag.objects.all()
    context = {'hashtags': hashtags}
    return render(request, 'todoapp/hashtags.html', context)


def task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'GET':
        return render(request, 'todoapp/task.html', {'task': task})
    elif request.method == 'POST':
        form = TaskForm(instance=task, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('todoapp:task',
                                        args=[task_id]))


def hashtag(request, hashtag_id):
    hashtag = get_object_or_404(Hashtag, id=hashtag_id)
    tasks_in_which_used = hashtag.task_set.all()
    context = {'hashtag': hashtag, 'tasks_in_which_used': tasks_in_which_used}
    return render(request, 'todoapp/hashtag.html',
                  context)


def new_task(request):
    form = TaskForm()
    content = {'form': form}
    return render(request, 'todoapp/new_task.html', content)


def new_hashtag(request):
    if request.method != 'POST':
        form = HashtagForm()
        content = {'form': form}
        return render(request, 'todoapp/new_hashtag.html', content)
    else:
        form = HashtagForm(data=request.POST)
        if form.is_valid():
            new_task = form.save(commit=True)
            return HttpResponseRedirect(reverse('todoapp:tasks'))


def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    form = TaskForm(instance=task)
    content = {'task': task, 'form': form}
    return render(request, 'todoapp/edit_task.html', content)
