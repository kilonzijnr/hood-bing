from django.db.models.signals import post_save
from django.dispatch import receiver
from models import Profile
from django.contrib.auth import get_user_model

from neighbourhood.views import UpdateUserProfile

User= get_user_model()

@receiver(post_save, sender=User, dispatch_uid='save_new_user_profile')
def save_profile(sender, instance, created, **kwargs):
    user = instance
    if created:
        profile = Profile(user=user)
        profile.save()