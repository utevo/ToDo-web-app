from django.contrib import admin
from django.urls import path

from . import views

app_name = 'todoapp'
urlpatterns = [
    # ex: /todo/
    path('', views.index, name='index'),
    # ex: /todo/task/3/
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),
    # ex: /todo/hashtag/1/
    path('hashtag/<int:hashtag_id>/', views.hashtag_detail,
         name='hashtag_detail'),
    path('new_task/', views.new_task, name='new_task')
]
