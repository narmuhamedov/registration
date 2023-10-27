from django.shortcuts import render, get_object_or_404
from .models import TodoModel
from .forms import TodoForm
from django.views import generic


#TODO LIST
class TodoListView(generic.ListView):
    template_name = 'todo_list.html'
    queryset = TodoModel.objects.all()

    def get_queryset(self):
        return TodoModel.objects.all()


#TODO ADD
class CreateTodoView(generic.CreateView):
    template_name = 'create_todo.html'
    form_class = TodoForm
    queryset = TodoModel.objects.all()
    success_url = '/todo_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateTodoView, self).form_valid(form=form)

#TODO DELETE
class DeleteTodoView(generic.DeleteView):
    template_name = 'confirm_delete.html'
    success_url = '/todo_list/'

    def get_object(self, **kwargs):
        todo_id = self.kwargs.get('id')
        return get_object_or_404(TodoModel, id=todo_id)

#TODO UPDATE
class UpdateTodoView(generic.UpdateView):
    template_name = 'update_todo.html'
    form_class = TodoForm
    success_url = '/todo_list/'

    def get_object(self, **kwargs):
        todo_id = self.kwargs.get('id')
        return get_object_or_404(TodoModel, id=todo_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateTodoView, self).form_valid(form=form)
