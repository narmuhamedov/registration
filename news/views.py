from django.shortcuts import render
from django.views import generic
from .models import Post
from .forms import PostFormView
class PostView(generic.ListView):
    template_name = 'news/news_list.html'
    queryset = Post.objects.filter().order_by('-id')

    def get_queryset(self):
        return Post.objects.filter().order_by('-id')


class CreatePostView(generic.CreateView):
    template_name = 'news/create_list.html'
    form_class = PostFormView
    queryset = Post.objects.all()
    success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreatePostView, self).form_valid(form=form)
