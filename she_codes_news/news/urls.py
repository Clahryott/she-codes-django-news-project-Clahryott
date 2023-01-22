from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [ #this is a specific url page
    path('', views.IndexView.as_view(), name='index'), #this is structured in the main urls sections (front door)
    path('<int:pk>/', views.StoryView.as_view(), name='story'), #int is the story number (integer) - pk is primary key which we've given a pk by number - ie story 1, story 2 etc. 3, 4, 5 etc. each story has a number. only one number per story
    path('add-story/', views.AddStoryView.as_view(), name='newStory'),
    #path('story/int:pk>/edit',views.EditStoryView.as_view(),name='editStory') slight amendment
    path('story/<int:pk>/edit/', views.EditStoryView.as_view(), name='editStory'),
    #path('edit_story/<int:story_id>/', views.edit_story, name='edit_story'), #didn't work- changed to above check naming convention???? /// 

    #to potentially add *****
    
    #path('all-stories/', views.All_stories_View.as_view(), name='allstories' ),
    #path('authors/<int:pk>/stories', views.AuthorStories.as_view(), name= 'authorstories' ),
    #path('<int:pk>/delete', views.DeleteStoryView.as_view(), name='deleteStory')
]

#no patterns/ path for each question
#only 1 url 