from django.db import models
from proyecto.models import Project
from requeriments.models import RF, RnF

# Create your models here.
class SRF(models.Model):
    title = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    rf = models.ForeignKey(RF, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    priority = models.CharField(max_length=100)
    state = models.CharField(max_length=100, default='Propuesta')
    cost = models.CharField(max_length=100)
    comments = models.CharField(max_length=100)
    input = models.CharField(max_length=200)
    output = models.CharField(max_length=200) 
    destiny = models.CharField(max_length=200) 
    process = models.CharField(max_length=200)
    restriction = models.CharField(max_length=200) 
    source = models.CharField(max_length=200) 
    collateral_damage = models.CharField(max_length=200)
  


    def __str__(self):
        return self.title

class SRFFile(models.Model):
    file = models.FileField(upload_to="specification")
    rf = models.ForeignKey(RF, on_delete=models.CASCADE, default=1)


class SRnF(models.Model):
    title = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    rnf = models.ForeignKey(RnF, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    type_r = models.CharField(max_length=100)
    sub_type = models.CharField(max_length=100)
    priority = models.CharField(max_length=100)
    state = models.CharField(max_length=100, default='Propuesta')
    cost = models.CharField(max_length=100)
    comments = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class SRnFFile(models.Model):
    file = models.FileField(upload_to="specification")
    rnf = models.ForeignKey(RnF, on_delete=models.CASCADE, default=1)

