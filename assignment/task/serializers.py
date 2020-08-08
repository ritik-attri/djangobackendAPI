from rest_framework import serializers
from .models import Task,TaskTracker
#Serializers for models

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields=('task_id','task_type','task_desc')
    def update(self, instance, validated_data):
        instance.task_desc=validated_data.get('task_desc',instance.task_desc)
        instance.save()
        return instance

class TaskTrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model=TaskTracker
        fields=('task_typeTracker','update_type','email')
