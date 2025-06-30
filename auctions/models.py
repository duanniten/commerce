from django.contrib.auth.models import AbstractUser
from django.db import models


class Category(models.Model):
    categories = models.CharField(max_length = 30)
    
    def __str__(self):
        return self.categories

class AuctionListings(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length= 30)
    description = models.TextField()
    imageUrl = models.CharField(blank= True, null= True)
    category = models.ForeignKey(Category, blank= True, on_delete=models.SET_NULL, null= True)
    creationTimestamp = models.DateTimeField(auto_now_add= True)
    timestamp = models.DateTimeField(auto_now = True)
    createUser = models.ForeignKey("User",on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class User(AbstractUser):
    watchlist = models.ManyToManyField(AuctionListings,blank=True)
    
    
class Bids(models.Model):
    bidValue = models.DecimalField(max_digits=12, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestand = models.DateTimeField(auto_now_add= True)
    listing = models.ForeignKey(AuctionListings, on_delete= models.CASCADE)


class Comments(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    timestamp  = models.DateTimeField(auto_now_add= True)
    listinig = models.ForeignKey(AuctionListings, on_delete=models.CASCADE)