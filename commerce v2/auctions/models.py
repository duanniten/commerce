from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    watchList = models.ManyToManyField("Listing")
    createdListings = models.ManyToManyField("Listing")
    wonListings = models.ManyToManyField("Listing")
    
