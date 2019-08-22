from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

app_name = 'users'
urlpatterns = [
    # ex /users/
    path('', views.index, name='index'),

    # ex /users/login/
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),

]
