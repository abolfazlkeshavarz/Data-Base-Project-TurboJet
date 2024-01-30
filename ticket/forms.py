from django import forms
from .models import Ticket
class QueryForm(forms.Form):
    from_location = forms.CharField(widget=forms.TextInput(attrs={
                'class': "input-group mb-3 input-group-text w-25",
                'style': "margin-left: auto; margin-right: auto; display: block; text-align: center;",
                'placeholder': 'From'}))
    to_location = forms.CharField(widget=forms.TextInput(attrs={
                'class': "input-group mb-3 input-group-text w-25",
                'style': "margin-left: auto; margin-right: auto; display: block; text-align: center;",
                'placeholder': 'To'}))
    date = forms.DateField(widget=forms.DateInput(attrs={
                'type': 'date',
                'class': "input-group mb-3 input-group-text w-25",
                'style': "margin-left: auto; margin-right: auto; display: block; text-align: center;",
                'placeholder': 'When'
                }))
    
