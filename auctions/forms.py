from .models import *
from django.forms import ModelForm
from django import forms

class CreateListinigForm(ModelForm):

    bid = forms.DecimalField(max_digits=10, decimal_places=2, min_value= 0)

    class Meta:
        model = AuctionListings
        fields = ['title', 'description', 'imageUrl', 'category']
        labels = {
            'title': 'Item',
            'description': 'Item description',
            'imageUrl': 'photo URL',
            'category' : 'Category'
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'}),
            
            'description': forms.TextInput(attrs={
                 'class': "form-control", "rows":"3"}),
            
            'bid': forms.TextInput(
                attrs={'class': 'form-control', 'step': '0.01'}),
            
            'imageUrl': forms.TextInput(attrs={
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