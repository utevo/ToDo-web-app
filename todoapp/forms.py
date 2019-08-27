from django import forms

from .models import Task, Hashtag

from django.core.exceptions import ValidationError


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed', 'hashtags', ]
        user : int

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user


    def clean(self):
        """
        Checks that all hashtags belong to the corect user
        """
        hashtags = self.cleaned_data.get('hashtags')
        for hashtag in hashtags: 
            print(hashtag.owner)
            print(self.user)
            if hashtag.owner != self.user:
                raise ValidationError("User don't own one of the hashtags.")


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