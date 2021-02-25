from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, PostUpdateForm
from django.urls import reverse_lazy

# Create your views here.
# def home(request):
#     return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-id']

class PostDetailView(DetailView):
    model = Post
    template_name = 'postDetail.html'

class PostCreateView(CreateView):
    model = Post
    template_name = 'postCreate.html'
    form_class = PostForm
    # fields = '__all__'
    # fields = ('title, 'body')

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'postUpdate.html'
    form_class = PostUpdateForm
    # fields = ['title', 'title_tag', 'body']

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'postDelete.html'
    success_url = reverse_lazy('home')