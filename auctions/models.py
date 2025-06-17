from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    categories = models.CharField(max_length = 30)
    
    def __str__(self):
        return self.categories

class AuctionListings(models.Model):
    title = models.CharField(max_length= 30)
    description = models.TextField()
    bid = models.DecimalField(max_digits=12, decimal_places= 2)
    imageUrl = models.CharField(blank=True, null= True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null= True)

    def __str__(self):
        return self.title


class Bids(models.Model):
    pass


class Comments(models.Model):
    pass