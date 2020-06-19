from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Categorie(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="images/categorie")
    date_add = models.DateTimeField(auto_now_add = True)
    date_up = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default= True)

    class Meta:
        verbose_name="Categorie"
        verbose_name_plural="Categories"

    def __str__(self):
        return self.nom

class Tag(models.model):
    nom = models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add = True)
    date_up = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default= True)

    class Meta:
        verbose_name="Tag"
        verbose_name_plural="Tags"
    
    def __str__(self):
        return self.nom
    

class Article(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to = "images/Article")
    contenu = models.TextField()
    category = models.foreignKey(Categorie, on_delete= models.CASCADE, related_name="category_Article")
    tag = models.ManyToManyField(Tag)
    date_add = models.DateTimeField(auto_now_add = True)
    date_up = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default= True)
    
    class Meta:
        verbose_name="Article"
        verbose_name_plural="Articles"
    
    def __str__(self):
        return self.nom

class Commentaire(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="article_commentaire")
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name="commentaire_User")
    image = models.ImageField(upload_to="images/commentaire")
    date_add = models.DateTimeField(auto_now_add = True)
    date_up = models.DateTimeField(auto_now = True)
    status = models.BooleanField(default= True)

     class Meta:
         verbose_name="Commentaire"
         verbose_name_plural="Commentaires"
    
    def __str__(self):
        return self.Commentaire