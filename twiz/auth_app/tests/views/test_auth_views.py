from django.test import TestCase, Client
from django.urls import reverse

class TestAuth(TestCase):

    client = Client()
    response = client.get(reverse('auth_app:auth_home'))

    def test_auth_home_200(self):
        self.assertEqual(
            self.response.status_code,
            200
        )