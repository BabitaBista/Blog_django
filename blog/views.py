from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.contrib.auth.models import User

from .models import Post

# Create your views here.

# posts = [
#     {
#         'author': 'Bobs',
#         'title': 'Blog Post Demo1',
#         'content': 'Content-post',
#         'date_posted': 'Jun 17'
#     },
#     {
#         'author': 'Jonny',
#         'title': 'Blog Post Demo2',
#         'content': 'Content-post',
#         'date_posted': 'Jun 17'
#     }
# ]

def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    param= {'name':'Babita'}
    return render(request, 'blog/home.html',context)

class PostListView(ListView):
    model = Post
    # app=blog, model=Post
    template_name = 'blog/home.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts' #home template posts
    ordering = ['-date_posted']
    paginate_by = 6

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        user = get_object_or_404(User, username= self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # function that run userPassesTestMixin to check if user passes certain condition
    def test_func(self):
        # post that we are currently trying to update
        post = self.get_object()
        #check if the author of the post is the user trying to update
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    # function that run userPassesTestMixin to see if user passes certain condition
    def test_func(self):
        # post that we are currently trying to update
        post = self.get_object()
        # check if the author of the post is the user trying to update
        if self.request.user == post.author:
            return True
        return False

def about(request):
    return render(request,'blog/about.html', {'title':'About-Page'})


