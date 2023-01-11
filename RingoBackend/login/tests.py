from django.test import TestCase
from login.constants import *
from login.models import User

# Create your tests here.
class SmokeTestCase(TestCase):
    def test_smoke(self):
        self.assertEqual(1+1, 2)

class LoginTest(TestCase):
    def setUp(self) -> None:
        user = User.objects.create_user()
        return super().setUp()
