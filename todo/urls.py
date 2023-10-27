from django.urls import path
from .views import TodoListView, CreateTodoView, DeleteTodoView,UpdateTodoView

urlpatterns = [
    path('todo_list/', TodoListView.as_view()),
    path('todo_list/<int:id>/delete/', DeleteTodoView.as_view()),
    path('todo_list/<int:id>/update/', UpdateTodoView.as_view()),
    path('create_todo/', CreateTodoView.as_view()),

]