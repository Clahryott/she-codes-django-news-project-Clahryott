from django import forms
from django.forms import ModelForm
from .models import NewsStory

class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'pub_date', 'image_url', 'content']
        widgets = {
            'pub_date': forms.DateInput(format=('%m/%d/%Y'), 
        attrs={'class':'form-control', 'placeholder':'Select a date','type':'date'}),
        }


#----NOTES-----
#build a comment system
#https://djangocentral.com/creating-comments-system-with-django/
