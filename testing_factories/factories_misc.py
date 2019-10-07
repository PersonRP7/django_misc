from django.test import TestCase
from django.urls import reverse
from users.models import CustomUser
from app.models import Picture
# from PIL import Image
import tempfile
# from django.core.files import File
# from model_mommy import mommy
# from model_mommy.recipe import Recipe, foreign_key
import factory
import random, string
from django.core.files.base import ContentFile
from django.contrib.auth import get_user_model
import PIL

# class CustomUserFactory(factory.DjangoModelFactory):

#     class Meta:
#         model = get_user_model()

# class PictureFactory(factory.DjangoModelFactory):

#     class Meta:
#         model = 'app.Picture'

#     user = factory.RelatedFactory(CustomUserFactory)
#     title = factory.Sequence(lambda x: '.'.join([random.choice(string.ascii_lowercase) for i in range(10)]))
#     image = factory.LazyAttribute(
#             lambda _: ContentFile(
#                 factory.django.ImageField()._make_data(
#                     {'width': 1024, 'height': 768}
#                 ), 'example.jpg'
#             )
#         )

# class TestPicture(TestCase):

#     def test_picture(self):
#         print(Picture.objects.first())
#         self.assertTrue(
#             Picture.objects.first()
#         )
# class TestUser(TestCase):

#     def test_user(self):
#         cuf = CustomUserFactory()
#         print(CustomUser.objects.first())
#         self.assertTrue(
#             CustomUser.objects.first()
#         )


# class CustomUserFactory(factory.DjangoModelFactory):

#     class Meta:
#         model = 'users.CustomUser'

#     username = factory.Sequence(lambda n: 'steve%s' % n)
#     email = factory.LazyAttribute(lambda o: '%s@example.org' % o.username)
#     password = factory.Sequence(lambda x: '.'.join([random.choice(string.ascii_lowercase) for i in range(10)]))


# class PictureFactory(factory.DjangoModelFactory):

#     class Meta:
#         model = Picture

#     user = factory.RelatedFactoryList(CustomUserFactory)
#     title = factory.Sequence(lambda x: ''.join([random.choice(string.ascii_lowercase) for i in range(10)]))
#     cover = factory.LazyAttribute(
#         lambda _: ContentFile(
#             factory.django.ImageField()._make_data(
#                 {'width':1024, 'height':768}
#             ), 'example.jpg'
#         )
#     )

# class TestPicture(TestCase):

#     def test_picture(self):
#         print(Picture.objects.first())
#         picture = PictureFactory()
#         self.assertTrue(
#             Picture.objects.first()
#         )

# class PictureFactory(factory.DjangoModelFactory):

#     class Meta:
#         model = 'app.Picture'

#     user = CustomUserFactory()
#     title = factory.Sequence(lambda x: ''.join([random.choice(string.ascii_lowercase) for i in range(10)]))
#     cover = 

# class TestUser(TestCase):

#     def test_user(self):
#         user = CustomUserFactory()
#         print(CustomUser.objects.first().password)
#         self.assertTrue(
#             CustomUser.objects.first()
#         )

# class TestPicture(TestCase):
#     #This works. Somewhat
#     def setUp(self):
#         # self.user = mommy.make(CustomUser)
#         self.picture = mommy.make('app.Picture')

#     def test_x(self):
#         # print(CustomUser.objects.first().email)
#         self.assertTrue(
#             CustomUser.objects.first()
#         )
 
#     def test_y(self):
#         print(Picture.objects.first().cover)
#         self.assertTrue(
#             Picture.objects.first()
#         )

        
# class TestSetup(TestCase):
    

# class TestSetup(TestCase):

#     def create_picture(self, user, title):
#         image = Image.new('RGB', (100, 100))
#         tmp_file = tempfile.NamedTemporaryFile(suffix = '.jpg')
#         Picture.objects.create(
#             user = user,
#             title = title,
#             cover = File(image)
#         )

#     def create_user(self, username, password, email):
#         CustomUser.objects.create_user(
#             username = username,
#             password = password,
#             email = email
#         )

#     def setUp(self):
#         self.create_user(
#             "user1", "testing321", "user1@email.com"
#         )
#         self.create_user(
#             "user2", "testing321", "user2@email.com"
#         )
#         self.user1 = CustomUser.objects.get(
#             username = "user1"
#         )
#         self.user2 = CustomUser.objects.get(
#             username = "user2"
#         )
#         self.create_picture(self.user1, "Picture One")

#     def test_pic(self):
#         self.assertTrue(
#             Picture.objects.get(
#                 title = "Picture One"
#             )
#         )

# class TestLoggedIn(TestSetup):

#     def setUp(self):
#         super().setUp()
#         self.client.login(
#             username = 'user1',
#             password = 'testing321',
#         )

#     def test_paginated_get(self):
#         response = self.client.get(
#             reverse(
#                 'paginated:paginated',
#                 kwargs = {"username":"user1"}
#             )
#         )
#         self.assertEqual(
#             response.status_code,
#             200
#         )

# class TestLoggedOut(TestCase):

#     def test_pagination_redirects_to_login(self):
#         response = self.client.get(
#             reverse('paginated:paginated',
#             kwargs = {"username":"user1"})
#          )
#         self.assertRedirects(
#             response,
#             '/users/login/?next=/paginated/user1',
#             status_code = 302,
#             target_status_code = 200
#         )
