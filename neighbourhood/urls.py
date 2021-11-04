from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('', views.user_signup, name= 'signup'),
    path('profile', profile, name = 'profile'),
    path('homepage', homepage, name = 'homepage'),
    path('profile/update/<int:pk>', UpdateUserProfile.as_view(), name = 'UpdateUserProfile'),
    path('business/update/<int:pk>', UpdateBusiness.as_view(), name = 'updatebusiness'),
    path('search/', search_results, name = 'search_business'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
