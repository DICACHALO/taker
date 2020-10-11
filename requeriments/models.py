from django.db import models
from proyecto.models import Project

# Create your models here.
class RF(models.Model):
    title = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    priority = models.CharField(max_length=100)
    state = models.CharField(max_length=100, default='Propuesta')
    cost = models.CharField(max_length=100)
    comments = models.CharField(max_length=100)
    specific = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class RnF(models.Model):
    title = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    type_r = models.CharField(max_length=100)
    priority = models.CharField(max_length=100)
    state = models.CharField(max_length=100, default='Propuesta')
    cost = models.CharField(max_length=100)
    comments = models.CharField(max_length=100)
    specific = models.BooleanField(default=False)

    def __str__(self):
        return self.title

