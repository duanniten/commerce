from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    watchList = models.ManyToManyField("Listing")
    createdListing = models.ManyToManyField("Listing")
    wonListing = models.ManyToManyField("Listing")
    
