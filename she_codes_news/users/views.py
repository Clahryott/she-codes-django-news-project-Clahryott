from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm
from news.models import NewsStory


class CreateAccountView(CreateView): #class based view
	form_class = CustomUserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'users/createAccount.html'

class AccountView(generic.DetailView): #specific user profile user
	model = CustomUser
	template_name = 'users/user_profile.html'
	context_object_name = 'user'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['user_stories'] = NewsStory.objects.filter(author=self.kwargs['pk'])
		return context

