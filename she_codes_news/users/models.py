from django.db import models  
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
        pass   #remind myself what this iis and why I don't need a long list of fields - do I need it? Kristy says no
        
        def __str__(self):
            return self.username


# profile model------ https://ordinarycoders.com/django-custom-user-profile#Adding%20a%20wishlist%20button%20to%20the%20products