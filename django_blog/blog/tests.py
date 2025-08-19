from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from.models import Post
 

'''''
WHY TESTS?
-Catch bugs, breaking changes before production
-Ensure correct status code , responses and permissions

TOOLS
-APIITestCase and APIClient from DRF

WHY DRF Test?
-JSON playload
-Authentication
-Serializers
'''

class PostAPITest(APITestCase):
    def test_create_post(self):
        url="/api/posts/"
        data = {"title": "test post", "content": "test content"}

        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Post.objects.count(), 1)