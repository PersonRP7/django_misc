from django.test import TestCase
from ..models import Plane
from django.contrib.auth.models import User
from ..signals import wrapper_around_handle_built_and_updated
from unittest.mock import patch
from django.db.models.signals import pre_save

class PlaneTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username = "user",
            password = "testing333"
        )

        self.plane = Plane.objects.create(
            owner = self.user,
            name = "plane0"
        )

    def test_pre_save_activates(self):
        with patch('five.signals.wrapper_around_handle_built_and_updated', autospec=True) as mocked_handler:
            pre_save.connect(mocked_handler, sender = Plane)
            Plane.objects.create(
                owner = self.user,
                name = "plane1"
            )
            self.assertEqual(mocked_handler.call_count, 1)

    def test_new_instance_str_method_no_update(self):
        instance = Plane.objects.get(id = 1)
        response = instance.__str__()
        self.assertNotIn(
            response,
            "updated"
        )

    def test_modified_instance_str_method_contains_updated(self):
        instance = Plane.objects.get(id = 1)
        instance.name = "new_plane_name"
        instance.save()
        self.assertIn(
            "updated",
            instance.__str__()
        )