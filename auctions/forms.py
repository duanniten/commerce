from .models import *
from django.forms import ModelForm
from django import forms

class MakeBid(ModelForm):
    class Meta:
        model = Bids
        fields = ["bidValue"]
        labels = {
            "bidValue" : "Make a new bid "
        }
        widgets = {
            "bidValue" : forms.NumberInput(attrs={ "class " : "form-control"})
        }

class CreateListinigForm(ModelForm):
    initialBid = forms.DecimalField(
        max_digits= 10, min_value= 0, decimal_places=2, label= "Initial Bid")
    class Meta:
        model = AuctionListings
        fields = ['title', 'description', 'imageUrl', 'category']
        labels = {
            'title': 'Item',
            'description': 'Item Description',
            'imageUrl': 'photo URL',
            'category' : 'Category'
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'}),
            
            'description': forms.Textarea(attrs={
                 'class': "form-control", "rows":"3"}),
                  
            'imageUrl': forms.URLInput(attrs={
                'class': 'form-control'}),

        }
        error_messages = {
            'title': {
                'required': 'Title is required!',
            },
            'description':{
                'required': 'Description is required!'
            },
            'bid':{
                'required': 'First price is required!'
            }
        }