from django.forms import ModelForm
from django import forms

from . import models

class CreateListing(ModelForm):
    initialBid = forms.DecimalField(
        max_digits=10, decimal_places=2, required=True
        )

    class meta():
        models = models.Listing
        fields = [
            "imageUrl",
            "title",
            "description"
        ]
