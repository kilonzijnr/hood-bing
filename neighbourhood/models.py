from os import name
from typing import ClassVar
from django.db import models
from cloudinary.uploader import upload
# Create your models here.

class Neighbourhood(models.Model):
    """Model class for Neighbourhood"""
    name = models.CharField(max_length= 70)
    location = models.CharField(max_length=70)
    occupants = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name

    def save_neighbourhood(self):
        self.save()

    def delete_neighbourhood(self):
        self.delete()

    @classmethod
    def update_neighbourhood(cls, neighbourhood_id, new_neighbourhood):
        """Method for updating a new Neighbourhood"""

        ghetto = cls.objects.filter(id = neighbourhood_id).update(name = new_neighbourhood)
        return ghetto

    @classmethod
    def update_occupants(cls, neighbourhood_id, new_occupants):
        """Method for updating new occupants"""

        ghetto = cls.objects.filter(id= neighbourhood_id).update(occupants = new_occupants)
        return ghetto

    @classmethod
    def find_neighbourhood(cls, search_term):
        """Method for finding a neighbourhood by searching"""
        jiji = cls.objects.filter(name__icontains = search_term)
        return jiji
