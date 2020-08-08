from django.shortcuts import render
from .models import TaskTracker,Task
from .serializers import TaskSerializer,TaskTrackerSerializer
from rest_framework import viewsets
#from assignment.settings import EMAIL_HOST_USER
#from django.core.mail import send_mail
import logging
logger = logging.getLogger(__name__)

# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskTrackerViewSet(viewsets.ModelViewSet):
    lookup_field = 'task_typeTracker'
    queryset = TaskTracker.objects.all()
    serializer_class = TaskTrackerSerializer

    def post(self, request):
        #mssg = 'Hey your task with tracker id {} is updated in {} days and the email is {}.'.format(
        #    request.data['task_typeTracker'], request.data['update_type'], request.data['email'])
        #send_mail(
        #    'Task Created',
        #    mssg,
        #    EMAIL_HOST_USER,
        #    [request.data['email']],
        #    fail_silently=False,
        #)
        return self.create(TaskTracker, **request.data)
    def put(self,request):
        #mssg = 'Hey your task with tracker id {} is updated in {} days and the email is {}.'.format(request.data['task_typeTracker'],request.data['update_type'],request.data['email'])
        #send_mail(
        #    'Task Updated',
        #    mssg,
        #    EMAIL_HOST_USER,
        #    [request.data['email']],
        #    fail_silently=False,
        # )
        return self.update(TaskTracker,**request.data)


