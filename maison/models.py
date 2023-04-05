from django.db import models
from django import forms
import json


# Create your models here.

CATEGORY =(
("M", "Maison"),
("A", "Studio"),
("S", "Studio"),
("C", "Chambre"),
)
class House(models.Model):
    category = models.CharField(max_length = 30, default='maison',choices=CATEGORY)
    image = models.ImageField()
    price = models.FloatField()
    description = models.TextField()
    ville = models.CharField(max_length=50)
    quartier = models.CharField(max_length=200)
    Nom_proprio = models.CharField(max_length=50)
    tel_proprio = models.IntegerField(default='698575401')
    date_added =models.DateTimeField(auto_now=True)
 
    class Meta:
        ordering = ['-date_added']


class meubles(models.Model):
    
    image = models.ImageField()
    price = models.FloatField()
    description = models.TextField()
    ville = models.CharField(max_length=50)
    quartier = models.CharField(max_length=200)
    Nom_entreprise = models.CharField(max_length=50)
    tel_entreprise = models.IntegerField(default='698575401')
    date_added =models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-date_added']
