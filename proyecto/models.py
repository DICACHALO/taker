from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse



# Create your models here.

class Project(models.Model):

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500, null=True)
    user = models.ManyToManyField(User,through='User_Project',related_name='users',blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
   
    def __str__(self):
        return self.title



class User_Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    type_user = models.CharField(max_length=100, default='Gerente')



