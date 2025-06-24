from .models import *
from django.forms import ModelForm
from django import forms

class CreateListinigForm(ModelForm):
    bid = forms.DecimalField(label='Initial Bid', decimal_places=2, max_digits=10)

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