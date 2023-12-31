from django.shortcuts import render
from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from . import forms


# Logout
class AuthLogoutView(LogoutView):
    next_page = reverse_lazy('users:home')

#Registrations
class RegisterationView(CreateView):
    form_class = forms.CustomUserForm
    success_url = '/users/'
    template_name = 'registration.html'

#Login
class AuthLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse('users:post')

#UserList
class PostView(ListView):
    queryset = User.objects.filter().order_by("-id")
    template_name = 'post.html'

    def get_queryset(self):
        return User.objects.filter().order_by("-id")
