from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import PostForm

# Create your views here.
# def home(request):
#     return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'postDetail.html'

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'postCreate.html'
    # fields = '__all__'
    # fields = ('title, 'body')