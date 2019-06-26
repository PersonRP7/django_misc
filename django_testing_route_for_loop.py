from django.test import TestCase
from django.urls import reverse
from ..models import Product
from rest_framework import status

def test_delete_everything_204(self):
        for item in Product.objects.all():
            response = self.client.delete(
                reverse('delete', kwargs = {'pk':item.pk}),
                content_type = 'application/octet-stream',
                follow = True
            )
            self.assertEqual(
                response.status_code,
                status.HTTP_204_NO_CONTENT
            )