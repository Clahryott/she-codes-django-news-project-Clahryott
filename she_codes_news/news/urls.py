from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [ #this is a specific url page
    path('', views.IndexView.as_view(), name='index'), #this is structured in the main urls sections (front door)
    path('<int:pk>/', views.StoryView.as_view(), name='story'), #int is the story number (integer) - pk is primary key which we've given a pk by number - ie story 1, story 2 etc. 3, 4, 5 etc. each story has a number. only one number per story
    path('add-story/', views.AddStoryView.as_view(), name='newStory'),
    path('story/int:pk>/edit',views.EditStoryView.as_view(),name='editStory')
    #path('edit_story/<int:story_id>/', views.edit_story, name='edit_story'), #didn't work- changed to abovecheck naming convention???? /// 
]

#no patterns/ path for each question
#only 1 url 