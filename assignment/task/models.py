from django.db import models
from uuid import uuid4
# Create your models here.
class Task(models.Model):
    task_id=models.CharField(max_length=100,unique=True,blank=True,default=uuid4,primary_key=True)
    task_type=models.IntegerField(choices=[(1,'Type_1'),(2,'Type_2'),(3,'Type_3'),(4,'Type_4')])
    task_desc=models.CharField(max_length=200)

class TaskTracker(models.Model):
    task_typeTracker=models.OneToOneField(Task,on_delete=models.CASCADE,related_name='task_typeTracker',primary_key=True)
    update_type=models.IntegerField(choices=[(1,'per_Day'),(7,'per_Week'),(30,'per_Monthly')])
    email=models.EmailField(max_length=100,blank=True)