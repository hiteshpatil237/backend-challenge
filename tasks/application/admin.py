from django.contrib import admin
from .models import Task, Label

# Register your models here.

admin.site.register(Task)
admin.site.register(Label)