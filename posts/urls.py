from django.urls import path
from .views import *

urlpatterns = [
    path('', all_post_view, name='users_posts'),
    path('<int:pk>/', post_detail_view, name='user_post_detail'),
    path('create_post', create_post_view, name='create_post'),
    path('<int:pk>/edit', update_post_view, name='update_post'),
    path('<int:pk>/delete', delete_post_view, name='delete_post'),
]
