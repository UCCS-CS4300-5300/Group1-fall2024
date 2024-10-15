from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

from .models import *

class UserTestCase(TestCase):
    def setUp(self):
        self.test_user = User.objects.create(
            username = "test_user",
            email = "test@user.com",
            password = "test1234",
        )

    def test_user_created(self):
        self.assertEqual(self.test_user.username, "test_user")
        self.assertEqual(self.test_user.password, "test1234")
        self.assertEqual(self.test_user.email, "test@user.com")


class IndexTestCase(TestCase):
    def test_index_view(self):
        client = Client()
        response = client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cookapp/index.html')
