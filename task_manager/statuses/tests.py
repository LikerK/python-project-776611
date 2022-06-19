from django.test import TestCase
from django.urls import reverse
from .models import Status
from task_manager.tasks.models import Task
from task_manager.users.models import User

# Create your tests here.
OK_CODE = 200
REDIRECT_CODE = 302


class StatusTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(
            username='user',
            password='password',
        )
        status_for_task = Status.objects.create(
            name='test_status_in_task'
        )
        task = Task.objects.create(
            name='test_task',
            status=status_for_task,
            author=user,
        )
        status = Status.objects.create(
            name='test_status2'
        )
        self.client.force_login(user)


    def test_statuses_list(self):
        response = self.client.get(reverse('statuses:list'))
        self.assertEqual(response.status_code, OK_CODE)
        self.assertQuerysetEqual(
            response.context_data['object_list'],
            Status.objects.all(),
            ordered=False,
        )
    

    def test_create_status(self):
        response = self.client.get(reverse('statuses:create'))
        self.assertEqual(response.status_code, OK_CODE)
        response = self.client.post(reverse('statuses:create'), data={
            'name': 'test_status3'
            },)
        self.assertEqual(response.status_code, REDIRECT_CODE)
        self.assertEqual('test_status3', Status.objects.get(pk=3).name)
    

    def test_updage_status(self):
        response = self.client.get(reverse('statuses:change', args='1'))
        self.assertEqual(response.status_code, OK_CODE)
        response = self.client.post(reverse('statuses:change', args='1'), data={
            'name': 'test_change_status'
            },)
        self.assertEqual(response.status_code, REDIRECT_CODE)
        self.assertEqual('test_change_status', Status.objects.get(pk=1).name)
    

    def test_delete_status(self):
        response = self.client.get(reverse('statuses:delete', args='2'))
        self.assertEqual(response.status_code, OK_CODE)
        response = self.client.post(reverse('statuses:delete', args='2'))
        self.assertEqual(response.status_code, REDIRECT_CODE)

        with self.assertRaises(Status.DoesNotExist):
            Status.objects.get(pk=2)

    
    def test_delete_status_in_task(self):
        response = self.client.get(reverse('statuses:delete', args='1'))
        self.assertEqual(response.status_code, OK_CODE)
        response = self.client.post(reverse('statuses:delete', args='1'))
        self.assertEqual(response.status_code, REDIRECT_CODE)
        self.assertEqual('test_status_in_task', Status.objects.get(pk=1).name)