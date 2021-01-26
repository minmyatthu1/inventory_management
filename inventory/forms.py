from .models import Inventory
from django import forms
from django.forms import ModelForm


class Inventory_form(forms.ModelForm):

    class Meta:
        model = Inventory
        fields = ['item_detail', 'operation', 'price', 'comments']
        widgets = {
            'item_detail': forms.TextInput(attrs={'class': 'form-control'}),
            'operation': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'comments': forms.NumberInput(attrs={'class': 'form-control'}),
        }
