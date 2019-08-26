from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404

from .models import Task, Hashtag
from .forms import TaskForm, HashtagForm
from .forms import DeleteTaskForm, DeleteHashtagForm, TickTaskForm

from django.contrib.auth.decorators import login_required


def index(request):
    return HttpResponseRedirect(reverse('todoapp:tasks'))

@login_required
def tasks(request):
    if request.method == 'GET':
        all_tasks_not_completed = Task.objects.filter(completed=False)
        tasks_not_completed = all_tasks_not_completed.filter(
            owner=request.user)

        all_tasks_completed = Task.objects.filter(completed=True)
        tasks_completed = all_tasks_completed.filter(owner=request.user)

        context = {
            'tasks_not_completed': tasks_not_completed,
            'tasks_completed': tasks_completed,
            }
        return render(request, 'todoapp/tasks.html', context)

    if request.method == 'POST':
        form = TaskForm(data=request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.owner = request.user
            new_task.save()
            form.save_m2m()
            return HttpResponseRedirect(reverse('todoapp:tasks'))

@login_required
def hashtags(request):
    if request.method == 'GET':
        hashtags = Hashtag.objects.all()
        context = {'hashtags': hashtags}
        return render(request, 'todoapp/hashtags.html', context)

    if request.method == 'POST':
        form = HashtagForm(data=request.POST)
        if form.is_valid():
            new_hashtag = form.save(commit=True)
            return HttpResponseRedirect(reverse('todoapp:hashtags'))

@login_required
def task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if task.owner != request.user:
        raise Http404

    if request.method == 'GET':
        tick_task_form = TickTaskForm(instance=task)

    if request.method == 'POST':

        # user want tick on/off task
        if 'tick_task_form' in request.POST: 
            task.completed = not task.completed
            task.save() # Should I check form?
            return HttpResponseRedirect(reverse('todoapp:task',
                                        args=[task_id]))
        else: # user want to create new task
            form = TaskForm(instance=task, data=request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('todoapp:task',
                                            args=[task_id]))

    context = {'task': task, 'tick_task_form': tick_task_form}
    return render(request, 'todoapp/task.html', context)

@login_required
def hashtag(request, hashtag_id):
    hashtag = get_object_or_404(Hashtag, id=hashtag_id)
    tasks_in_which_used = hashtag.task_set.all()

    if request.method == 'GET':
        context = {
                    'hashtag': hashtag,
                    'tasks_in_which_used': tasks_in_which_used,
                    }
        return render(request, 'todoapp/hashtag.html',
                        context)

    if request.method == 'POST':
        form = HashtagForm(instance=hashtag, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('todoapp:hashtag',
                                        args=[hashtag_id]))

@login_required
def new_task(request):
    form = TaskForm()
    content = {'form': form}
    return render(request, 'todoapp/new_task.html', content)

@login_required
def new_hashtag(request):
    form = HashtagForm()
    content = {'form': form}
    return render(request, 'todoapp/new_hashtag.html', content)

@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if task.owner != request.user:
        raise Http404

    form = TaskForm(instance=task)
    content = {'task': task, 'form': form}
    return render(request, 'todoapp/edit_task.html', content)

@login_required
def edit_hashtag(request, hashtag_id):
    hashtag = get_object_or_404(Hashtag, id=hashtag_id)

    form = HashtagForm(instance=hashtag)
    content = {'hashtag': hashtag, 'form': form}
    return render(request, 'todoapp/edit_hashtag.html', content)

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if request.method == 'GET':
        form = DeleteTaskForm(instance=task)
        context = {'task': task, 'form': form}
        return render(request, 'todoapp/delete_task.html', context)

    if request.method == 'POST':
        form = DeleteTaskForm(data=request.POST, instance=task)

        if form.is_valid():
            task.delete()
            return HttpResponseRedirect(reverse('todoapp:tasks'))

@login_required
def delete_hashtag(request, hashtag_id):
    hashtag = get_object_or_404(Hashtag, id=hashtag_id)

    if request.method == 'GET':
        form = DeleteHashtagForm(instance=hashtag)
        context = {'hashtag': hashtag, 'form': form}
        return render(request, 'todoapp/delete_hashtag.html', context)

    if request.method == 'POST':
        form = DeleteHashtagForm(data=request.POST, instance=hashtag)

        if form.is_valid():
            hashtag.delete()
            return HttpResponseRedirect(reverse('todoapp:hashtags'))
