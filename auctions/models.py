from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    categories = models.CharField(max_length = 30)
    
    def __str__(self):
        return self.categories


class Bids(models.Model):
    bidValue = models.DecimalField(max_digits=12, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Comments(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    date = models.DateTimeField(auto_now=True, auto_now_add= True)

class AuctionListings(models.Model):
    title = models.CharField(max_length= 30)
    description = models.TextField()
    bid = models.DecimalField(max_digits=12, decimal_places= 2)
    imageUrl = models.CharField(blank= True, null= True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank= True, null= True)
    coments = models.ManyToManyField(Comments, blank=True, null= True)

    def __str__(self):
        return self.title