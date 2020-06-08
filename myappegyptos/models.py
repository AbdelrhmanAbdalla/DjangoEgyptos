from django.db import models

# Create your models here.
class Ville(models.Model):
    name = models.CharField(max_length=20, default=None)
    description = models.CharField(max_length=100, default=None)
    imgVille = models.ImageField(upload_to='images_places', blank=True)
    price = models.CharField(max_length=30, default=None)

    def __str__(self):
        return self.name

class Joueur(models.Model):
    name = models.CharField(max_length=20, default=None)
    description = models.CharField(max_length=100, default=None)
    imgJoueur = models.ImageField(upload_to='images_joueur', blank=True)
    club = models.CharField(max_length=30,default=None)
    pays = models.CharField(max_length=20,default=None)

    def __str__(self):
        return self.name