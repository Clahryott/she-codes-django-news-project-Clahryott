from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm


class IndexView(generic.ListView):
    template_name = 'news/index.html' #which is telling me to use the index view

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) #this potentially could be the individual in () 
        context['latest_stories'] = NewsStory.objects.all()[:4]
        context['old_stories'] = NewsStory.objects.all().order_by ('pub_date')[:4]
        return context

    #NOTE 
    #no specific story, it's all listed, no http responses, no import?  check examples, can use function based views.... similar
    #where to go to find index template, in class index view 


class StoryView(generic.DetailView):
    model = NewsStorytemplate_name = 'news/story.html'
    context_object_name = 'story'

class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user #means the user that is logged in
        return super().form_valid(form)