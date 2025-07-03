from django.contrib.auth.models import AbstractUser
from django.db import models

class AuctionListing(models.Model):
    id = models.AutoField(primary_key=True)

    title = models.CharField(max_length= 30)
    description = models.TextField()
    imageUrl = models.CharField(blank= True, null= True)
    creationTime = models.DateTimeField(auto_now_add= True)
    timestamp = models.DateTimeField(auto_now = True)

    category = models.ForeignKey("Category", blank= True, on_delete=models.SET_NULL, null= True)
    createUser = models.ForeignKey("User",on_delete=models.CASCADE)
    biggerBid = models.ForeignKey("Bid", on_delete= models.SET_NULL) # mudar para procurar outra bid

    def __str__(self):
        return self.title

class User(AbstractUser):
    watchlist = models.ManyToManyField(AuctionListing,blank=True)

class Category(models.Model):
    categories = models.CharField()

class Comments(models.Model):
    listing = models.ForeignKey(AuctionListing, on_delete= models.CASCADE)
    text = models.TextField(max_length = 500)
    timestamp = models.DateTimeField(auto_now_add=True)

class Bid(models.Model):
    listing = models.ForeignKey(AuctionListing, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits= 10, decimal_places= 2)