from django.forms import ModelForm
from django import forms

from . import models

class CreateListing(ModelForm):
    initialBid = forms.DecimalField(
        max_digits=10, decimal_places=2, required=True
        )

    class Meta:
        models = models.Listing
        fields = [
            "imageUrl",
            "title",
            "description"
        ]

class ChangeListing(ModelForm):
    def __init__(self, bidValue, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bidValue = bidValue + 0.01
        self.fields['value'].widget.attrs.update({
            "min" : self.bidValue,
            "max" : self.bidValue
        })
    class Meta:
        models = models.Bids
        fields = [
            "value"
        ]
        widgets = {
            "value" : forms.NumberInput(attrs={
                "class" : "form-control"
            })
        }