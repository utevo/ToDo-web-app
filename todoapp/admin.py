from django.contrib import admin

from todoapp.models import Task, Hashtag 

# Register your models here.


admin.site.register(Task)

admin.site.register(Hashtag)