from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import Profile, Business, Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import Widget

#Create your forms here

class ReqistrationForm(UserCreationForm):
    """A Form for user registration"""
    class Meta:
        model = User
        fields = ['first_name', 'sur_name', 'email','username', 'password', 'confirm_password']

        widgets = {
            'first_name':forms.TextInput(attrs = {'class':'form-control names', 'placeholder':"First Name", 'label': 'First Name'}),
            'sur_name':forms.TextInput(attrs = {'class':'form-control names', 'placeholder':"Second Name", 'label': 'Sur Name'}),
            'email':forms.TextInput(attrs = {'class':'form-control names', 'placeholder':"Email Address", 'label': 'Email Address'}),
            'username':forms.TextInput(attrs = {'class':'form-control names', 'placeholder':"Username", 'label': 'Username'}),
            'password':forms.PasswordInput(attrs = {'class':'form-control names','type':'password', 'placeholder':"Password", 'label': 'Password'}),
            'confirm_password':forms.PasswordInput(attrs = {'class':'form-control names', 'placeholder':"Confirm Password", 'label': 'Confirm Password'}),
        }

class ProfileUpdateForm(forms.ModelForm):
    """A Form for User Profile Update"""

    class Meta:
        model = Profile
        fields = ('neighbourhood', 'profile_photo')

        widgets = {
            'neighborhood': forms.Select(attrs={'class':"form-control profile", 'label': 'Neighborhood', 'placeholder':"Input Your Neighborhood", 'aria-label':"Neighborhood"}),
            'profile_photo': forms.FileInput(attrs = {'class': 'form-control photo', 'type': 'file'}),
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



        



