import json

from django.contrib.auth.models import User
from .models import Content, Rating
from rest_framework import status
from .serializers import ContentSerializer
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import AccessToken

from django.urls import reverse


def generate_jwt_token(user):
    access = AccessToken.for_user(user)
    return str(access)


class ContentApiViewSetTestCase(APITestCase):
    def setUp(self):
        self.title = "Radiohead - Creep"
        self.description = "A popular song."
        self.category = "M"
        self.content_1 = Content.objects.create(
            title=self.title, description=self.description, category=self.category
        )
        self.user_1 = User.objects.create_user(username="Andrew")

    def test_retrieve(self):
        jwt_token = generate_jwt_token(self.user_1)
        url = reverse("content-detail", args=[self.content_1.id])
        contents = Content.objects.filter(id=self.content_1.id).first()

        response = self.client.get(url, HTTP_AUTHORIZATION=f"Bearer {jwt_token}")

        serializer_data = ContentSerializer(contents).data

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_create(self):
        old_content_num = Content.objects.all().count()
        jwt_token = generate_jwt_token(self.user_1)
        url = reverse("content-list")
        data = {
            "title": "Muse - Hysteria",
            "description": "A cool song",
            "category": "M",
        }
        json_data = json.dumps(data)

        response = self.client.post(
            path=url,
            HTTP_AUTHORIZATION=f"Bearer {jwt_token}",
            data=json_data,
            content_type="application/json",
        )

        cur_content_num = Content.objects.all().count()

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(old_content_num + 1, cur_content_num)


class RatingApiViewSetTestCase(APITestCase):
    def setUp(self):
        self.title = "Alone in the Dark"
        self.description = "A popular video game."
        self.category = "G"
        self.content_1 = Content.objects.create(
            title=self.title, description=self.description, category=self.category
        )
        self.user_1 = User.objects.create_user(username="Dan")

    def test_create(self):
        old_rating_num = Rating.objects.all().count()
        jwt_token = generate_jwt_token(self.user_1)
        url = reverse("rating-list")
        data = {"content": self.content_1.id, "rated_by": self.user_1.id, "rating": "5"}
        json_data = json.dumps(data)

        response = self.client.post(
            path=url,
            HTTP_AUTHORIZATION=f"Bearer {jwt_token}",
            data=json_data,
            content_type="application/json",
        )

        cur_rating_num = Content.objects.all().count()

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(old_rating_num + 1, cur_rating_num)
