from django.contrib import admin
from .models import Project, User_Project

# Register your models here.
admin.site.register(Project)
admin.site.register(User_Project)