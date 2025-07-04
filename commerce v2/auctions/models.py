from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    watchList = models.ManyToManyField("Listing")
    
class Bids(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=10, decimal_places= 2)
    listing = models.ForeignKey('Listing', on_delete=models.CASCADE)

class Comment(models.Model):
    timestamp =  models.DateTimeField(auto_now_add= True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    listing = models.ForeignKey('Listing', on_delete=models.CASCADE)

class Listing(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    changeTimestamp = models.DateTimeField(auto_now=True)
    imageUrl = models.URLField()
    title = models.CharField(max_length=64)
    description = models.TextField()
