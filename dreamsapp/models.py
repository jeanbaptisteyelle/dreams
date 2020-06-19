from django.db import models

# Create your models here.
class Service(models.Model):
    nom = models.CharField(max_length = 255)
    description = models.TextField()
    image = models.ImageFeld(upload_to = "images/service")
    date_add = models.DateTimeField(auto_now_add = True)
    date_up = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default= True)
    
    class Meta: 
        verbose_name = "service"
        verbose_name_plural = "services"
    
    def __str__(self):
        return self.nom

class Type(models.Model):
    nom = models.CharField(max_length=50)
    date_add = models.DateTimeField(auto_now_add = True)
    date_up = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default= True)
    class Meta:
        verbose_name = "type"
        verbose_name_plural = "types"
    
    def __str__(self):
        return self.nom

class Project(models.Model):
    types = models.ForeignKey(Type, on_delete =models.CASCADE, related_name="types_project")
    nom = models.CharField(max_length=255)
    image = models.ImageFeld(upload_to="images/project")
    
    class Meta:
        verbose_name = "project"
        verbose_name_plural = "projects"
    
    def __str__(self):
        return self.project

class Appartment(models.Model):
    nom = models.CharField(max_length=255)
    superficie = models.FloatField()
    douche = models.FloatField()
    garage = models.FloatField()
    like = models.IntegerField()
    description =  models.TextField()
    date_add = models.DateTimeField(auto_now_add = True)
    date_up = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default= True)

    class Meta:
        verbose_name = "appartment"
        verbose_name_plural = "appartments"

    def __str__(self):
        return self.nom


