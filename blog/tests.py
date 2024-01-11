from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Post

class PostAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_post(self):
        data = {'title': 'Test Post', 'content': 'This is a test post content.'}
        response = self.client.post('/api/posts/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.get().title, 'Test Post')
