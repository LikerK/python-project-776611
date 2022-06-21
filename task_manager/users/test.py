from django.test import TestCase
from django.urls import reverse
from .models import User

OK_CODE = 200
REDIRECT_CODE = 302

NEW_USER = {
    'first_name': 'test_first_name',
    'last_name': 'test_last_name',
    'username': 'test_username',
    'password1': 'test_password',
    'password2': 'test_password',
}

CHANGE_USER = {
    'first_name': 'test_update',
    'last_name': 'test_update',
    'username': 'test_update',
    'password1': 'test_password',
    'password2': 'test_password',
}


class UserTestCase(TestCase):
    def setUp(self):
        """Set up method for testing."""
        first_user = User.objects.create(
            first_name='Djon',
            last_name='Snow',
            username='DjonSnow',
            password='firstuserpassword',
        )
        first_user.save()
        second_user = User.objects.create(
            first_name='Ariya',
            last_name='Stark',
            username='AriyaStark',
            password='seconduserpassword',
        )
        second_user.save()

    def test_home_page(self):
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
        respone = self.client.post(reverse('users:create'), data=NEW_USER,)
        self.assertEqual(respone.status_code, REDIRECT_CODE)
        self.assertEqual(
            NEW_USER['first_name'],
            User.objects.get(pk=3).first_name
        )
        self.assertEqual(
            NEW_USER['last_name'],
            User.objects.get(pk=3).last_name
        )
        self.assertEqual(
            NEW_USER['username'],
            User.objects.get(pk=3).username
        )

    def test_change_user(self):
        self.client.force_login(User.objects.get(pk=1))
        response = self.client.get(reverse('users:change', args='1'))
        self.assertEqual(response.status_code, OK_CODE)
        response = self.client.post(
            reverse('users:change', args='1'),
            data=CHANGE_USER
        )
        self.assertEqual(
            CHANGE_USER['first_name'],
            User.objects.get(pk=1).first_name
        )
        self.assertEqual(
            CHANGE_USER['last_name'],
            User.objects.get(pk=1).last_name
        )
        self.assertEqual(
            CHANGE_USER['username'],
            User.objects.get(pk=1).username
        )

    def test_delete_user(self):
        self.client.force_login(User.objects.get(pk=1))
        response = self.client.get(reverse('users:delete', args='1'))
        self.assertEqual(response.status_code, OK_CODE)
        response = self.client.post(reverse('users:delete', args='1'))
        self.assertEqual(response.status_code, REDIRECT_CODE)
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(pk=1)

    def test_another_delete_user(self):
        self.client.force_login(User.objects.get(pk=1))
        response = self.client.get(reverse('users:delete', args='2'))
        self.assertEqual(response.status_code, REDIRECT_CODE)
    
    def test_user_login(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, OK_CODE)
        self.assertTemplateUsed(response, template_name='form.html')
        print(User.objects.get(pk=1).username)
        response = self.client.post(reverse('login'), data={
            'username': 'DjonSnow',
            'password': 'firstuserpassword',
        },
        )
        self.assertEqual(response.status_code, REDIRECT_CODE)
