from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm
#from .forms import CustomerUserChangeForm ----= where is this?
from news.models import NewsStory

# to add ???

#from django.shortcuts import render, redirect
#from django.contrib.auth import views as auth_views
#from django.contrib.auth.forms import PasswordChangeForm


class CreateAccountView(CreateView): #class based view
	form_class = CustomUserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'users/createAccount.html'

#class EditAccountView(generic.UpdateView):
    #form_class = CustomUserChangeForm
    #model = CustomUser
    #context_object_name = 'createAccount'
    #template_name = 'users/createAccount.html'
    #def get_success_url(self): 
         #return reverse_lazy('users:profile', kwargs={'pk': self.object.id})


class AccountView(generic.DetailView): #specific user profile user (account or also could be refer to as Profile)
	model = CustomUser
	template_name = 'users/user_profile.html'
	context_object_name = 'user'
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['user_stories'] = NewsStory.objects.filter(author=self.kwargs['pk'])
		return context

def ChangePasswordDoneView(request):
    return render(request, 'users/changePassword_done.html', {})

def ChangePasswordView(request):
    if request.method == 'POST':
        form = auth_views.PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:changePassword_done')
    else:
        form = auth_views.PasswordChangeForm(request.user)
    return render(request, 'users/changePassword.html', {'form': form})

