from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=25, default='Rico')
    last_name = models.CharField(max_length=25, blank=True)
    hair_color = models.CharField(max_length=10, blank=True)
    eye_color = models.CharField(max_length=10)
    age = models.IntegerField()
    height = models.CharField(max_length=6)
    favorite_animal = models.CharField(max_length=25, blank=True)
    number_of_animals = models.IntegerField(null=True)
