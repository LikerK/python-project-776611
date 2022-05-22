from django.test import TestCase, Client
from ..models import User


# Create your tests here.
class TestUser(TestCase):
    fixtures = ['users.json']

    def setUp(self) -> None:
        self.name = User.objects.get()
        