from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user
from django.contrib.messages import get_messages
from .models import User


OK_CODE = 200
REDIRECT_CODE = 302


class UserTestCase(TestCase):
    def setUp(self):
        """Set up method for testing."""
        user = User.objects.create(
            first_name='Djon',
            last_name='Snow',
            username='DjonSnow',
            password='NightWatch',
        )
        user.save()
    
    def test_home_page(self):
        """Test for checking main page."""

        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, OK_CODE)
        self.assertTemplateUsed(
            response, template_name='index.html'
        )
    
    def test_users_list(self):
        response = self.client.get(reverse('users:list'))
        self.assertEqual(response.status_code, OK_CODE)
        self.assertTemplateUsed(
            response, template_name='users.html'
        )
        user = User.objects.get(pk=1)
        self.assertEqual(user.username, 'DjonSnow')
        self.assertEqual(user.first_name, 'Djon')
        self.assertEqual(user.last_name, 'Snow')

    def test_create_user(self):
         response = self.client.get(reverse('users:create'))
         self.assertEqual(response.status_code, OK_CODE)
         self.assertTemplateUsed(
             response, template_name='form.html'
         )
         