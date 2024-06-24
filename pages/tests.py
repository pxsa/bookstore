from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class HomePageTest(TestCase):
    
    def test_home_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)


    def test_home_page_content(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'HOME')


    def test_home_page_url_by_path(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


    def test_home_page_template_used(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')