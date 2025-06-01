from django import forms
from .models import *
class UpdateCourFm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['photo', 'name', 'fee', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter Name'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
        }