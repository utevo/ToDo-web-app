from django.db import models
from django.utils import timezone

from django.contrib.auth.models import User

# Create your models here.

class Hashtag(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Task(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(null=False, blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    # The lower value of invalidity means the task is more important
    invalidity = models.PositiveIntegerField(blank=True, null=True)

    hashtags = models.ManyToManyField(Hashtag, blank=True)

    def __str__(self):
        return self.title

    def __lt__(self, other):
        if self.invalidity is None:
            return True
        if other.invalidity is None:
            return False
        return self.invalidity > other.invalidity

    # TODO: need to test
    # should be enough to prevent access to non-owned hashtags 
    def clean(self):
        for hashtag in self.hashtags.all():
            if hashtag.owner != self.owner:
                raise ValidationError("User don't own one of the hashtags.")

    class Meta:
        ordering = ["completed", "-created_at"]
        verbose_name_plural = "tasks"
