from inventory.models import Sell
from django import forms
from django.forms import ModelForm
from datetime import date



class Sell_form(forms.ModelForm):
    
    class Meta:
        model = Sell
        fields = ['inventory', 'sell_date']
        widgets = {
            'inventory': forms.TextInput(attrs={'class': 'form-control'}),
            'sell_date': forms.DateInput(attrs={'class':'form-control', 'type':'date', 'value': date.today()}),
     }

