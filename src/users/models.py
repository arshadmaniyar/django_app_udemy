from django.db import models
from django.contrib.auth.models import User
from localflavor.us.models import USStateField,USZipCodeField
from .utils import user_directory_path

class location(models.Model):
   address_1 = models.CharField(max_length=255, blank=True)
   address_2 = models.CharField(max_length=255, blank=True)
   city = models.CharField(max_length=100, blank=True)
   state = USStateField(blank=True)
   zip_code = USZipCodeField(blank=True)

   def __str__(self):
       return f"{self.address_1}, {self.address_2}, {self.state} {self.zip_code}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    photo = models.ImageField(null=True,upload_to=user_directory_path)
    bio = models.TextField( blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    location = models.OneToOneField(location, on_delete=models.SET_NULL, null=True, blank=True)

    