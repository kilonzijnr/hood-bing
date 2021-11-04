from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import Profile, Business, Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect

#Create your forms here

class RegistrationForm(UserCreationForm):
    """A Form for user registration"""
    class Meta:
        model = User
        fields = ['email','username', 'password', 'password2']

        widgets = {
            'email':forms.TextInput(attrs = {'class':'form-control names', 'placeholder':"Email Address", 'label': 'Email Address'}),
            'username':forms.TextInput(attrs = {'class':'form-control names', 'placeholder':"Username", 'label': 'Username'}),
            'password':forms.PasswordInput(attrs = {'class':'form-control names','type':'password', 'placeholder':"Password", 'label': 'Password'}),
            'confirm_password':forms.PasswordInput(attrs = {'class':'form-control names', 'placeholder':"Confirm Password", 'label': 'Confirm Password'}),
        }

class ProfileUpdateForm(forms.ModelForm):
    """A Form for User Profile Update"""

    class Meta:
        model = Profile
        fields = ('neighbourhood', 'profile_photo','email')

        widgets = {
            'neighbourhood': forms.Select(attrs={'class':"form-control profile", 'label': 'Neighbourhood', 'placeholder':"Input Your Neighbourhood", 'aria-label':"Neighborhood"}),
            'profile_photo': forms.FileInput(attrs = {'class': 'form-control photo', 'type': 'file'}),
            'email': forms.TextInput(attrs={'class':"form-control profile", 'label': 'Contact Details', 'placeholder':"Contact Details", 'aria-label':"Contact Details"}),
        }
        
class PostForm(forms.ModelForm):
    """A form for uploading posts"""

    class Meta:
        model = Post
        fields = ('title', 'details')

        widgets = {
            'title': forms.TextInput(attrs={'class':"form-control post", 'label': ' Post Title', 'placeholder':"Input Title...", 'aria-label':"Title"}),
            'details' : forms.Textarea(attrs={'class':"form-control post", 'label': 'Posts Details', 'placeholder':"Input Details...", 'aria-label':"Details"}),
        }

class BusinessForm(forms.ModelForm):
    """A Form for inputing Neigbourhood Businesses"""

    class Meta:
        model = Business
        fields = ('bs_name','about','bs_email','neighbourhood','bs_logo')
        
        widgets = {
            'bs_name': forms.TextInput(attrs={'class':"form-control hood", 'label': 'Business Name', 'placeholder':"Input Business Name", 'aria-label':"Business Name"}),
            'bs_email': forms.TextInput(attrs={'class':"form-control hood", 'label': 'Business Email / Contact', 'placeholder':"Input Business Contact ", 'aria-label':"Business Contact"}),
            'about': forms.Textarea(attrs={'class':"form-control hood", 'label': 'Business Description', 'placeholder':"Input Business Description", 'aria-label':"Business About"}),
            'neighbourhood': forms.Select(attrs={'class':"form-control hood", 'label': 'Business Neighborhood', 'placeholder':"Input Business Neighborhood", 'aria-label':"Business Neighborhood"}),
            'bs_logo': forms.FileInput(attrs = {'class': 'form-control hood', 'type': 'file', 'label': 'Business Logo', 'placeholder':" Choose Business Logo", 'aria-label':"Business Logo"}),
        }
        


        



