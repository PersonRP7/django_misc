from django.test import TestCase, Client
from django.urls import reverse

class TestViews(TestCase):

    client = Client()
    response = client.get(reverse('twizzy:home'))

    def test_home_200(self):
        self.assertEqual(
            self.response.status_code,
            200
        )

    def test_home_view_template(self):
        self.assertTemplateUsed(
            self.response,
            'twizzy/home.html'
        )


