#No 3 Step user - create forms for user login and updating

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email'] # can add 'bio', 'profile_picture', LinkedIn, Instagram - potentially === would need to create for reference can also be used in UserChangeForm
        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']