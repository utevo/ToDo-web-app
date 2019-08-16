from django import forms

from .models import Task, Hashtag


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'hashtags']

class HashtagForm(forms.ModelForm):
    class Meta:
        model = Hashtag
        fields = ['title',]
