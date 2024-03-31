from rest_framework import viewsets
from .serializers import TaskSerializer, LabelSerializer
from .models import Task, Label

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer

class LabelViewSet(viewsets.ModelViewSet):
    queryset = Label.objects.all().order_by('-created_at')
    serializer_class = LabelSerializer