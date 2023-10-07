from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    body = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='posts'
    )

    objects = models.Manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('user_post_detail', args=[str(self.id)])
