from django.db import models
from django.utils import timezone


# Create your models here.

class Hashtag(models.Model):
    title = models.CharField(max_length=30)
    created_at = models.DateTimeField(default=timezone.now)


class Task(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(null=False)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    hashtags = models.ManyToManyField(Hashtag)
