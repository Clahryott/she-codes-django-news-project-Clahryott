from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm
from users.models import CustomUser

class IndexView(generic.ListView):
    template_name = 'news/index.html' #which is telling me to use the index view

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) #this potentially could be the individual in () 
        context['latest_stories'] = NewsStory.objects.all().order_by('-pub_date')[:4]
        context['all_stories'] = NewsStory.objects.all().order_by('-pub_date')
        context['authors'] = CustomUser.objects.all()
        return context

    #2nd attempt at edit story function
#class EditStoryView(generic.UpdateView):
    #form_class = StoryForm
    #model = NewsStory
    #context_object_name = 'story'
    #template_name = 'news/edit_story.html'
    #success_url = reverse_lazy("news:newsStory")

        #def form_valid(self, form):
            #"""Save the form and redirect to the success URL"""
            # Save the updated form pk = self.kwargs.get("pk")
            #story = get_object_or_404(NewsStory,pk=pk)
            #form.instance.story = story
            #return super ().form_valid(form)
        
        #def get_success_rul(self) -> str:
            #pk = self.kwargs.get("pk")
            #return reverse_lazy("news:story",kwargs={"pk":pk}) 
 
class EditStoryView(generic.UpdateView):
    form_class = StoryForm
    model = NewsStory
    context_object_name = 'story'
    template_name = 'news/editStory.html'
    success_url = reverse_lazy("news:newsStory")

    def form_valid(self, form):
        """Save the form and redirect to the success URL."""
        # Save the updated form
        pk = self.kwargs.get("pk")
        story = get_object_or_404(NewsStory, pk=pk)
        form.instance.story = story
        return super().form_valid(form) 

    def get_success_url(self) -> str:
        pk = self.kwargs.get("pk")
        return reverse_lazy("news:story", kwargs={"pk":pk})
    
    #1st attempt TRIED edit here
    #def edit_story(request, story_id):
        #post = NewsStory.objects.get(id=story_id)

        #if request.method != 'POST':
            #form = StoryForm(instance=post)

       # else:
            #form = StoryForm(instance=post, data=request.POST) 
            #if form.is_valid():
                #form.save()
                # return redirect('news:index')

        #context = {'story': story, 'index': index, 'form': form}
        #return render(request, 'news/edit_story.html', context)
   
    #no specific story, it's all listed, no http responses, no import?  check examples, can use function based views.... similar
    #where to go to find index template, in class index view 


class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

    ##build a comment system
    #1 comment
    def post_detail(request, slug):
        post = get_object_or_404(NewsStory, slug=slug)
        comments = post.comments.filter(active=True)
        template_name = 'news/story.html'
        new_comment = None
        #comment posted
        if request.method == 'POST':
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():

                # Create comment object, but don't save to database yet
                new_comment = comment_form.save(commit=False)
                # Assign the current post to comment
                new_comment.post = post
                # Save the comment to the database
                new_comment.save()
        else:
            comment_form = CommentForm()

        return render(request, template_name, {'NewsStory': NewsStory, 'comments': comments, 'new_comment': new_comment, 'comment_form': comment_form})


#class StoryView(generic.DetailView):

class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index') #

    def form_valid(self, form):
        form.instance.author = self.request.user #means the user that is logged in
        return super().form_valid(form)

#***** to add in ***

#class AuthorStories (generic.ListView): 
    #template_name = 'news/authorstories.html'
    #context_object_name = 'stories'

    #def get_queryset(self):
       #return NewsStory.objects.filter(author=self.kwargs['pk'])
       
#class DeleteStoryView(generic.DeleteView):
    #model = NewsStory
    #context_object_name = 'story'
    #template_name = 'news/deleteStory.html' 
    #success_url = reverse_lazy('news:index')