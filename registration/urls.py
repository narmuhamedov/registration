from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('registration/', views.RegisterationView.as_view()),
    path('', views.AuthLoginView.as_view(), name='login'),
    path('logout/', views.AuthLogoutView.as_view(), name='logout'),
    path('users/', views.PostView.as_view(), name='post'),
]