from django.urls import path
from .views import CreateAccountView, AccountView, ChangePasswordDoneView, ChangePasswordView #still needs to be added

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('<int:pk>', AccountView.as_view(), name='user_profile')
]