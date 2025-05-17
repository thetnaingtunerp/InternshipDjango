from django import forms
from .models import *
class PostCreateForm(forms.Form):
    title = forms.CharField()
    body = forms.CharField()
    photo = forms.ImageField()
    
class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['photo','title', 'post_body']
        
class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'post_body','photo1','photo2','photo3']
        
class BlogModelForm1(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'photo1']