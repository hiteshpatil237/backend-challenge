from django.db import models

# Create your models here.
class Label(models.Model):
    name = models.CharField(max_length=100, unique=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    completion_status = models.BooleanField(default=False)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    labels = models.ManyToManyField(Label)

    def __str__(self):
        return self.title