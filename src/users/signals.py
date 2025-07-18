from django.contrib.auth.models import User
from django.db.models.signals import post_save
from .models import Profile,location
from django.dispatch import receiver
@receiver(post_save, sender=User)

def create_user_profile(sender, instance, created, **kwargs): 
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=Profile)
def create_profile_location(sender, instance, created, **kwargs):
    if created:
       Profile_location = location.objects.create()
       instance.location = Profile_location
       instance.save()

@receiver(post_save, sender=Profile)
def delete_user_location(sender, instance, **kwargs):
    """
    Deletes the user location when the user is deleted.
    """
    if instance.location:
        instance.location.delete()