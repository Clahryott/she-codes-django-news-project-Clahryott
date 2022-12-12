from django import forms
from django.forms import ModelForm
from .models import NewsStory, Comment

class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'pub_date', 'image_url', 'content']
        widgets = {
            'pub_date': forms.DateInput(format=('%m/%d/%Y'), 
        attrs={'class':'form-control', 'placeholder':'Select a date','type':'date'}),
        }


#build a comment system
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
        labels = {'name':('Name'),'email':('Email'), 'body': ('Write your Comment'),}