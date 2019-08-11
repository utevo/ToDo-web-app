from django.db import models
from django.utils import timezone


# Create your models here.

class Hashtag(models.Model):
    title = models.CharField(max_length=30, unique=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title



class Task(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(null=False, blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    priority = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["completed", "-created_at"]
        verbose_name_plural = "tasks"

    hashtags = models.ManyToManyField(Hashtag, blank=True)
