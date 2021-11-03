from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.views.generic import UpdateView
from .forms import  PostForm, RegistrationForm, BusinessForm ,ProfileUpdateForm
from .models import Post, Profile,Neighbourhood, Business
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect
from django.contrib import messages
from django.urls.base import reverse

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
            return redirect('homepage')

    return render(request, 'login.html')

@login_required('')
def homepage(request):

    user = request.user

    posts = Post.objects.all()
    jiji = Neighbourhood.objects.all()
    
    manyposts = Post.objects.last()
    manybusinesses = Business.objects.last()

    upload_form = PostForm()

    if request.method == 'POST':
        upload_form = PostForm(request.POST)
        if upload_form.is_valid():
            profile = Profile.objects.filter(user = user).first()
            ghetto = profile.neighbourhood
            new_post = upload_form.save(commit= False)
            new_post.jiji = ghetto
            new_post.posted_by = Profile.objects.get(user = request.user)
            new_post.save()
            return HttpResponseRedirect(reverse('homepage'))
        else:
            upload_form = PostForm()

    return render(request, 'homepage.html',{'upload_form':upload_form, 'manyposts':manyposts, 'manybusinesses':manybusinesses, 'posts':posts,})


@login_required
def profile(request):
    """Function for displaying  User Profile Details"""

    user = request.user

    posts = Post.objects.filter(posted_by = profile).all()
    businesses = Business.objects.filter(owner = user).all()

    title = f'{request.user.username}\'s Profile'

    profileupdate = ProfileUpdateForm()
    businessupdate = BusinessForm()

    if request.method == 'POST':
        businessupdate = BusinessForm(request.POST, request.FILES)
        if businessupdate.is_valid():
            business = businessupdate.save(commit=False)
            business.manager = user
            business.save()
            return redirect('profile')
        else:
            businessupdate = BusinessForm()

    return render(request, 'profile.html', {'title':title, 'profile':profile, 'posts':posts, 'profileupdate':profileupdate, 'businessupdate':businessupdate, 'businesses':businesses})

class UpdateBusiness(LoginRequiredMixin, UpdateView):
    """A class view for updating bussiness profile"""

    model = Business
    form_class = Business
    template_name = 'business_update.html'
    context_object_name = 'business'

class UpdateUserProfile(LoginRequiredMixin,UpdateView):
    """A class view for updating user profile"""

    model = Profile
    form_class = 'ProfileUpdateForm'
    template_name = 'profile_update.html'
    context_object_name = 'profile'

@login_required
def search_results(request):
    """Function for searching for business profile"""

    if 'search_business' in request.GET and request.GET["search_business"]:
        search_term = request.GET.get("search_business")
        searched_business = Business.search_by_name(search_term)
        message = f"{search_term}"
        title = search_term
        return render(request, 'search.html',{"message": message, "Enter Valid Business Input": searched_business, 'title': title})
    else:
        message = "Enter a valid business input"
        return render(request, 'search.html',{"message": message}) 

def user_logout(request):
    """A function for signing out of user profile"terminating current session"""
    logout(request)
    return redirect('login')
