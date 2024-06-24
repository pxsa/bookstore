from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your tests here.
class TestSignUpPage(TestCase):

    username = 'myusername'
    email = 'myusername@gmail.com'

    def test_signup_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)


    def test_signup_url_by_path(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)


    def test_signup_page_form(self):
        model = get_user_model()
        user = model.objects.create_user(
            self.username,
            self.email,
        )

        self.assertEqual(model.objects.all().count(), 1)
        self.assertEqual(model.objects.all().first(), user)
        self.assertEqual(model.objects.all().first().username, self.username)
        self.assertEqual(model.objects.all().first().email, self.email)