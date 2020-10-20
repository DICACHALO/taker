from django.db import models
from proyecto.models import Project
from django.contrib.auth.models import User

# Create your models here.
class Mensaje(models.Model):
    nombre = models.CharField(max_length=200, default="user")
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    mensaje = models.TextField()
    created = models.TimeField(auto_now_add=True)

class UserMensaje(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    email = models.CharField(max_length=200, default="user")
    problema = models.TextField()
    created = models.TimeField(auto_now_add=True)
