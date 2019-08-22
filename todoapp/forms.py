from django import forms

from .models import Task, Hashtag


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed', 'hashtags', ]


class HashtagForm(forms.ModelForm):
    class Meta:
        model = Hashtag
        fields = ['title', ]


class DeleteTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = []


class DeleteHashtagForm(forms.ModelForm):
    class Meta:
        model = Hashtag
        fields = []


class TickTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = []