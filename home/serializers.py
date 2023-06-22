from rest_framework import serializers
from .models import Task


#Create serializer class for APIs
class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['task_title', 'task_description', 'due_date', 'tags', 'status']
