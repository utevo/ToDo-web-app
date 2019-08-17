from django.contrib import admin
from django.urls import path

from . import views

app_name = 'todoapp'
urlpatterns = [
    # ex: /todo/
    path('', views.index, name='index'),

    # ex: /todo/tasks/
    path('tasks/', views.tasks, name='tasks'),

    # ex: /todo/task/3/
    path('task/<int:task_id>/', views.task, name='task'),

    # ex: /todo/hashtag/1/
    path('hashtag/<int:hashtag_id>/', views.detail_hashtag,
         name='detail_hashtag'),

    # ex /todo/new_task/
    path('new_task/', views.new_task, name='new_task'),

    # ex /todo/new_hashtag/
    path('new_hashtag/', views.new_hashtag, name='new_hashtag'),

    # ex /todo/tasks/3/edit/
    path('task/<int:task_id>/edit/', views.edit_task, name='edit_task'),

]
