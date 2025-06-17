from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Category(models.Model):
    categories = models.CharField(max_length = 30)


class AuctionListings(models.Model):
    title = models.CharField(max_length= 30)
    description = models.TextField()
    bid = models.PositiveIntegerField()
    imageUrl = models.CharField(blank=True)
    category = models.ForeignKey(Category, blank=True)

    
class Bids(models.Model):
    pass


class Comments(models.Model):
    pass