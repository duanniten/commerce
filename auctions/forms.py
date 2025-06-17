from models import *
from django.forms import ModelForm
from django import forms

class CreateListinigForm(ModelForm):
    class Meta:
        model = AuctionListings
        fields = ['title', 'description', 'bid', 'imageUrl', 'category']
        labels = {
            'title': 'Item',
            'description': 'Item description',
            'bid': 'Current Price',
            'imageUrl': 'photo URL'
        }
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control'}),
            
            'description': forms.TextInput(attrs={
                 'class': "form-control", 'type': "file", 'id': "formFile", "rows":"3"}),
            
            'bid': forms.TextInput(
                attrs={'class': 'form-control', 'step': '0.01'}),
            
            'imageUrl': forms.TextInput(attrs={
                'class': 'form-control', "type":"file", "id":"formFile"}),
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