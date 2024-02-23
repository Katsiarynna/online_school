from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from .consts import USER_DATA, create_user


class CreateUserTest(APITestCase):
    def test_create_user(self):
        url = reverse('user-list')
        response = self.client.post(url, data=USER_DATA, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ReadUserTest(APITestCase):
    def setUp(self):
        self.user = create_user()

    def test_read_user_list(self):
        url = reverse('user-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_read_user_detail(self):
        url = reverse('user-detail', args=[self.user.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
