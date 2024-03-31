from rest_framework import serializers
from .models import Task, Label

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completion_status', 'owner', 'labels']

class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = ['name', 'owner']    