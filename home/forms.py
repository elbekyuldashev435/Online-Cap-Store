from django import forms
from .models import About


class AboutViewForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ['image', 'first_name', 'last_name', 'title']