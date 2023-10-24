from django.shortcuts import render
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.urls import reverse_lazy

class AuthLogoutView(LogoutView):
    next_page = reverse_lazy('users:post')


class RegisterationView(CreateView):
    form_class = UserCreationForm
    success_url = '/users/'
    template_name = 'registration.html'

class AuthLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse('users:post')





class PostView(ListView):
    queryset = User.objects.all()
    template_name = 'post.html'
    def get_queryset(self):
        return User.objects.all()