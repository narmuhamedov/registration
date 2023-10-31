from django.urls import path
from .views import PostView,CreatePostView

urlpatterns = [
    path('', PostView.as_view()),
    path('create_news/', CreatePostView.as_view()),
]