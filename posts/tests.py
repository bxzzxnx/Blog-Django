from django.test import TestCase
from .models import Post
from django.contrib.auth import get_user_model
from django.urls import reverse


class PostTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(
            username='test_user',
            email='test_email@example.com',
            password='test_password'
        )

        self.post = Post.objects.create(
            title='Title Test',
            description='Post description',
            body='Post body',
            author=self.user
        )

        self.client.force_login(self.user)

    def test_content(self):
        self.assertEqual(f'{self.post.title}', 'Title Test')
        self.assertEqual(f'{self.post.body}', 'Post body')
        self.assertEqual(f'{self.post.author}', 'test_user')

    def test_post_list_view(self):
        response = self.client.get(reverse('users_posts'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Post body')
        self.assertTemplateUsed(response, 'post.html')

    def test_post_exists(self):
        response = self.client.get('/post/1/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Title Test')
        self.assertTemplateUsed(response, 'post_detail.html')

    def test_get_absolute_url(self):
        self.assertEqual(self.post.get_absolute_url(), '/post/1/')

    def test_create_new_post(self):
        response = self.client.post(reverse('create_post'), {
            'title': 'Test Title',
            'description': 'Test Description',
            'body': 'Test body',
            'author': self.user
        })

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/post/2/')

    def test_update_post(self):
        new_data = {
            'title': 'New Title',
            'description': 'New Description',
            'body': 'New Body'
        }

        url = reverse('update_post', kwargs={'pk': self.post.pk})
        response = self.client.post(url, data=new_data)

        self.post.refresh_from_db()
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/post/1/')

        self.assertEqual(self.post.title, 'New Title')
        self.assertEqual(self.post.description, 'New Description')
        self.assertEqual(self.post.body, 'New Body')

    def test_delete_post(self):
        resp = self.client.get(
            reverse('delete_post', args='1'))
        self.assertEqual(resp.status_code, 200)
