from django.urls import include,path
from rest_framework import routers
from .views import TaskViewSet,TaskTrackerViewSet

#Routes
tasks=routers.DefaultRouter()
tasks.register('',TaskViewSet)
tasktracker=routers.DefaultRouter()
tasktracker.register('',TaskTrackerViewSet)

urlpatterns = [
    path('tasks/',include(tasks.urls)),
    path('tasktracker/',include(tasktracker.urls))
]