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





