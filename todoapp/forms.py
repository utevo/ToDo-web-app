from django import forms
from django.forms import ModelMultipleChoiceField
from django.forms.widgets import SelectMultiple

from .models import Task, Hashtag

from django.core.exceptions import ValidationError


class TaskForm(forms.ModelForm):

    _user : int
    hashtags : ModelMultipleChoiceField

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._user =  user
        self.fields['hashtags'] = ModelMultipleChoiceField(
                            queryset=Hashtag.objects.filter(owner=self._user), 
                            widget=SelectMultiple(),
                            required=False,
                            )

    class Meta:
        model = Task
        fields = ['title', 'description', 'completed', 'hashtags', ]

    def clean(self):
        """
        Checks that all hashtags belong to the corect user
        """
        hashtags = self.cleaned_data.get('hashtags')
        
        for hashtag in hashtags:
            if hashtag.owner != self._user:
                raise ValidationError(
                    "User don't own one of the hashtags.")


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
