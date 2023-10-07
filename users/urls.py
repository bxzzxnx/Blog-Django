from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/', users_page_view, name='users_page'),
    path('signup/', sign_up_view, name='signup'),
]
