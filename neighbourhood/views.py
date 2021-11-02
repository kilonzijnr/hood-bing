from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .forms import  PostForm, RegistrationForm, BusinessForm ,ProfileUpdateForm
from .models import Post, Profile,Neighbourhood, Business
from django.contrib.auth.decorators import login_required
from django.http.response import Http404
from django.contrib import messages

# Create your views here.

def signup(request):
    """A function for Initialising user registrationn form"""

    register = RegistrationForm()

    if request.method == 'POST':
        register = RegistrationForm(request.POST)
        if register.is_validd():
            register.save()
            user = register.cleaned_data.get('username')
            messages.success(request, user + 'You have succesfully created your account')
            return redirect('login')

    return render(request, 'signup.html', {'register':register})

def userlogin(request):
    """A function for initialising User Login Form"""

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password=password)

        if user is not None:
            login(request,user)
            return redirect('home')

    return render(request, 'login.html')
