from django.test import TestCase
from .. import forms

class TestSignupFormTooSimilar(TestCase):

    def test_signup_form_too_similar(self):
        form_data = {
            "email":"email@gmail.com",
            "first_name":"admin",
            "last_name":"admin",
            "username":"admin",
            "password1":"admin",
            "password2":"admin"
        }
        form = forms.SignupForm(data = form_data)
        self.assertFalse(form.is_valid())
        self.assertIn(
            'password2',
            form.errors.keys()
        )
        err_msgs = [
            'The password is too similar to the username.',
            'This password is too short. It must contain at least 8 characters.',
            'This password is too common.',
        ]
        for err in err_msgs:
            self.assertIn(
                err,
                form.errors['password2']
            )
