from django import forms
from django.db import models
from django.forms import fields
from .models import Form

class ContactForm(forms.ModelForm):
    class Meta:
        model=Form
        fields="__all__"