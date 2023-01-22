from django.contrib.auth import get_user_model
from django.db import models
#from django.urls import reverse

class NewsStory(models.Model):
    class Meta:
        ordering = ['-pub_date']
    
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField()
    content = models.TextField()
    image_url = models.URLField(blank=True)

    def __str__(self): #display the story title - self is the item class is changing***
        return self.title

    # def get_absolute_url(self):
    #     return reverse('news:story', kwargs={'pk':self.pk}) 

#what is textfield? no definitions  - no answer 

#-----NOTES------
#build a comment system 
#Add a view that processes the form and saves the new comment to the database.
#https://djangocentral.com/creating-comments-system-with-django/

class Comment(models.Model):
    post = models.ForeignKey(NewsStory,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
