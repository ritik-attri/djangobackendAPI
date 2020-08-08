from django.contrib import admin
from .models import TaskTracker,Task
# Register your models here.
admin.register(Task)
admin.register(TaskTracker)