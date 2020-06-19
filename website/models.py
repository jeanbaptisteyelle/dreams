from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class About(models.Model):
    image = models.ImageField(upload_to="images/about")
    titre = models.CharField(max_length = 255)
    descrption = models.TextField()
    date_add = models.DateTimeField(auto_now_add = True)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default= True)
    
    class Meta:
        verbose_name = "About"
        verbose_name_plural = "Abouts"

    def __str__(self):
        return self.titre

class Siteinfo(models.Model):
    slogan = models.CharField(max_length = 255)
    logo = models.ImageField(upload_to="images/siteinfo")
    phone = models.FloatField(max_length = 255)
    email = models.EmailField()
    mapping = models.TextField()
    image = models.ImageField()
    message = models.TextField()
    contact = models.FloatField()
    adresse = models.CharField(max_length = 255)
    date_add = models.DateTimeField(auto_now_add = True)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default= True)


    class Meta:
        verbose_name = "siteinfo"
        verbose_name_plural = "siteinfos"
    
    def __str__(self):
        return self.slogan

class Contact(models.Model):
    message = models.TextField()
    nom = models.CharField(max_length = 255)
    email = models.EmailField()
    sujet = models.TextField()
    date_add = models.DateTimeField(auto_now_add = True)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default= True)

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return self.nom

class Newletter(models.Model):
    email = models.EmailField()
    date_add = models.DateTimeField(auto_now_add = True)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default= True)

    class Meta:
        verbose_name = "Newletter"
        verbose_name_plural = "Newletters"
    
    def __str__(self):
        return self.Newletter

class Reseau_social(models.Model):
    nom = models.CharField(max_length= 255)
    lien = models.URLField()
    date_add = models.DateTimeField(auto_now_add = True)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default= True)

    icon = [
        ('facebook','fa-facebook'),
        ('fa-tweeter'),
        ('fa-globe'),
        ('fa-behance ')
    ]

    class Meta:
        verbose_name = "Reseau_social"
        verbose_name_plural = "Reseau_socials"

    def __str__(self):
        self.nom

class Temoignage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_temoignage')
    message = models.TextField()
    date_add = models.DateTimeField(auto_now_add = True)
    date_update = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default= True)

    class Meta:
        verbose_name = "Temoignage"
        verbose_name_plural = "Temoignages"
    
    def __str__(self):
        return self.Temoignage
