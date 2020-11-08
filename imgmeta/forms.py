from django.forms import ModelForm
from django import forms
from .models import *

class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageSet
        fields = ('image',)

class SearchForm(forms.Form):
     searchtext = forms.CharField(max_length=140,widget=forms.Textarea(attrs={'rows':'3', }),label="Search Text")