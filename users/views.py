# from django.views.generic import DetailView, CreateView
# from django.urls import reverse_lazy
# from django.contrib import messages

from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model, get_user
from .forms import *

''' Class Based Views

class UsersPageView(DetailView):
    context_object_name = 'user'
    model = get_user_model()
    template_name = 'user_post.html'

class SignUpView(CreateView):
    form_class = UserForm
    success_url = reverse_lazy('home')
    template_name = 'signup.html'

'''

# Function Based Views


def users_page_view(request, pk):
    obj = get_object_or_404(get_user_model(), id=pk)
    if obj != get_user(request):
        raise PermissionDenied
    return render(request, 'user_post.html', {'user': get_user_model().objects.get(id=pk)})


def sign_up_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = UserForm()
    return render(request, 'signup.html', {'form': form})
