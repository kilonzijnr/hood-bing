from django.contrib import admin
from .models import Neighbourhood,Business,Post, Profile

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Neighbourhood)
admin.site.register(Business)