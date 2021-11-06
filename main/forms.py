from django import forms
from django.contrib.auth import models
from .models import ContactProfile

class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=100,required=True,
        widget=forms.TextInput(attrs={
            "placeholder": "Full Name..",
        }))
    email = forms.EmailField(max_length=254,required=True,
        widget=forms.TextInput(attrs={
            "placeholder": "Email..",
        }))
    message = forms.CharField(max_length=1000,required=True,
        widget=forms.Textarea(attrs={
            "placeholder": "Message..",
            "rows":6,
        }))
    
    class Meta:
        model = ContactProfile
        fields = ("name","email","message",)

 