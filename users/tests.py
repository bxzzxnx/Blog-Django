from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class SignUpTest(TestCase):
    username = 'test_user'
    email = 'test_user@example.com'
    password = 'test_password'

    def test_signup_page_status_code(self):
        response = self.client.get('/users/signup/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_signup_form(self):
        new_user = get_user_model().objects.create(
            username=self.username,
            email=self.email
        )

        user = get_user_model().objects.all()

        self.assertEqual(user.count(), 1)
        self.assertEqual(user[0].username, new_user.username)
        self.assertEqual(user[0].email, new_user.email)
