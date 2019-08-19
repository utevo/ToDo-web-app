from django.contrib import admin
from django.urls import path

from . import views

app_name = 'todoapp'
urlpatterns = [
    # ex: /todo/
    path('', views.index, name='index'),

    # ex: /todo/tasks/
    path('tasks/', views.tasks, name='tasks'),

        # ex: /todo/hashtags/
    path('hashtags/', views.hashtags, name='hashtags'),

    # ex: /todo/task/3/
    path('task/<int:task_id>/', views.task, name='task'),

    # ex: /todo/hashtag/1/
    path('hashtag/<int:hashtag_id>/', views.hashtag, name='hashtag'),

    # ex /todo/new_task/
    path('new_task/', views.new_task, name='new_task'),

    # ex /todo/new_hashtag/
    path('new_hashtag/', views.new_hashtag, name='new_hashtag'),

    # ex /todo/tasks/3/edit/
    path('task/<int:task_id>/edit/', views.edit_task, name='edit_task'),

    # ex /todo/hashtag/1/edit/
    path('hashtag/<int:hashtag_id>/edit/', views.edit_hashtag, 
         name='edit_hashtag'),

    # ex /todo/task/3/delete/
    path('task/<int:task_id>/delete/', views.delete_task, name='delete_task'),

]
