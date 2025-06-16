from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Post


class PostAPITestCase(APITestCase):
    def setUp(self):
        self.post_data = {
            "title": "Test Post",
            "content": "This is a test post content.",
            "author": "Test Author",
        }

    def test_create_post(self):
        url = reverse("posts-list")
        response = self.client.post(url, self.post_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(Post.objects.first().title, self.post_data["title"])

    def test_list_posts(self):
        Post.objects.create(title="Post 1", content="Content 1", author="Author 1")
        Post.objects.create(title="Post 2", content="Content 2", author="Author 2")

        url = reverse("posts-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_delete_post(self):
        post = Post.objects.create(
            title="To Delete", content="Will be deleted.", author="Author 3"
        )
        url = reverse("posts-detail", args=[post.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.count(), 0)
