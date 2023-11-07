from django.urls import path
from .views import LinkListCreateView, LinkRetrieveView

urlpatterns = [
    path('links/', LinkListCreateView.as_view(), name='link-list-create'),
    path('links/<int:pk>/', LinkRetrieveView.as_view(), name='link-retrieve'),
]