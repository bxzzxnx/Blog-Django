# from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.urls import reverse_lazy

from .models import Post
from .forms import PostForm
from django.core.exceptions import PermissionDenied
from django.contrib.auth import get_user
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect


'''  Class Based Views

class AllPostsViews(LoginRequiredMixin, ListView):
    login_url = 'home'
    model = Post
    context_object_name = 'users'
    template_name = 'post.html'


class PostDetailView(LoginRequiredMixin, DetailView):
    login_url = 'home'
    model = Post
    template_name = 'post_detail.html'


class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    login_url = 'home'
    fields = ('title', 'description', 'body', )
    template_name = 'post_create.html'

    def form_valid(self, form):
        form.instance.author = get_user(self.request)
        return super().form_valid(form)


class UpdatePostView(LoginRequiredMixin, UpdateView):
    login_url = 'home'
    model = Post
    fields = ('title', 'description', 'body', )
    template_name = 'post_update.html'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class DeletePostView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('users_posts')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
'''

# Function Based Views


@login_required(login_url='home')
def all_post_view(request):
    return render(request, 'post.html', {'users': Post.objects.all()})


@login_required(login_url='home')
def post_detail_view(request, pk):
    return render(request, 'post_detail.html', {'post':  Post.objects.get(id=pk)})


@login_required(login_url='home')
def create_post_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        form.instance.author = get_user(request)

        if form.is_valid():
            form.save()
            return redirect('user_post_detail', form.save().pk)

    else:
        form = PostForm()
    return render(request, 'post_create.html', {'form': form})


@login_required(login_url='home')
def delete_post_view(request, pk):
    obj = get_object_or_404(Post, id=pk)
    if obj.author != get_user(request):
        raise PermissionDenied
    if request.method == 'POST':
        obj.delete()
        return redirect('users_posts')
    else:
        redirect('users_posts')
    return render(request, 'post_delete.html', {'post': obj})


@login_required(login_url='home')
def update_post_view(request, pk):
    obj = get_object_or_404(Post, id=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('user_post_detail', form.save().pk)
    else:
        if obj.author != get_user(request):
            raise PermissionDenied
        form = PostForm(instance=obj)

    return render(request, 'post_update.html', {'form': form})
