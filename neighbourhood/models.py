from os import name
from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import EmailField
from django.urls import reverse
# from cloudinary.models import CloudinaryField

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


class Profile(models.Model):
    """Model for User Profile"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, default = 'user')
    neighbourhood = models.ForeignKey(Neighbourhood, null =  True, blank=True, on_delete=models.DO_NOTHING, related_name = 'jiji')
    email = EmailField()
    profile_photo = models.ImageField(upload_to='images/')
    date_created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('profile')

    def __str__(self) -> str:
        return self.user.username

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def update_profile(cls, profile_id, new_profile):
        """Method for updating User Profile"""

        profile = cls.objects.filter(id = profile_id).update(user = new_profile)
        return profile

    @classmethod
    def search_by_username(cls, search_term):
        """Method for getting a user by username through search functionality"""

        users = cls.objects.filter(user__username__icontains = search_term)
        return users


class Business(models.Model):
    """Model for Business Profile"""

    bs_name = models.CharField(max_length= 70)
    neighbourhood = models.ForeignKey(Neighbourhood, null= True, on_delete= models.DO_NOTHING)
    bs_email = EmailField()
    manager = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    about = models.TextField(null= True)
    bs_logo =  models.ImageField(upload_to='images/')

    def __str__(self) ->str:
        return self.bs_name

    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def update_business(cls, business_id, new_business):
        """Method for updating business profile"""

        business = cls.objects.filter(id = business_id).update(name = new_business)
        return business

    @classmethod
    def search_by_name(cls, search_term):
        """Method for getting business profile through search functionality"""

        business = cls.objects.filter(bs_name__icontains =search_term)
        return business

class Post(models.Model):
    """Model for Post Uploads"""

    title = models.CharField(max_length= 70)
    details = models.TextField()
    jiji = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, null=True, blank=True)
    publishing_date = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()
        
