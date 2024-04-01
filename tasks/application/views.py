from rest_framework import viewsets
from .serializers import TaskSerializer, LabelSerializer
from .models import Task, Label

class OwnerFilterMixin:
    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        return queryset.filter(owner=user).order_by('id') if user.is_authenticated else queryset.none()

class TaskViewSet(OwnerFilterMixin, viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class LabelViewSet(OwnerFilterMixin, viewsets.ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer