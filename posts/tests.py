from django.test import TestCase
from django.urls import reverse

from .models import Post
# Create your tests here.

class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text='This is a test!')

    def test_model_content(self):
        self.assertEqual(self.post.text, 'This is a test!')

    def test_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepage(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'posts/post_list.html')
        self.assertContains(response, self.post.text)