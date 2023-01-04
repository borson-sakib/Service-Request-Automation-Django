from django import forms
from .models import User

class ImageForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['image1', 'imagelocation']