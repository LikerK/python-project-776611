from django.test import TestCase
from django.urls import reverse
from .models import Label
from task_manager.statuses.models import Status
from task_manager.users.models import User
from task_manager.tasks.models import Task


# Create your tests here.
OK_CODE = 200
REDIRECT_CODE = 302


class LabelsTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(
            username='user',
            password='password',
        )
        status_for_task = Status.objects.create(
            name='test_status_in_task'
        )
        label_for_task = Label.objects.create(
            name='test_label_in_task',
        )
        Label.objects.create(
            name='test_label1',
        )
        task = Task.objects.create(
            name='test_task',
            status=status_for_task,
            author=user,
        )
        task.labels.add(label_for_task)
        self.client.force_login(user)

    def test_labels_list(self):
        response = self.client.get(reverse('labels:list'))
        self.assertEqual(response.status_code, OK_CODE)
        self.assertQuerysetEqual(
            response.context_data['object_list'],
            Label.objects.all(),
            ordered=False,
        )

    def test_create_label(self):
        response = self.client.get(reverse('labels:create'))
        self.assertEqual(response.status_code, OK_CODE)
        response = self.client.post(reverse('labels:create'), data={
            'name': 'test_status3'
        },
        )
        self.assertEqual(response.status_code, REDIRECT_CODE)
        self.assertEqual('test_status3', Label.objects.get(pk=3).name)

    def test_updage_label(self):
        response = self.client.get(reverse('labels:change', args='1'))
        self.assertEqual(response.status_code, OK_CODE)
        response = self.client.post(reverse('labels:change', args='1'), data={
            'name': 'test_change_status'
        },
        )
        self.assertEqual(response.status_code, REDIRECT_CODE)
        self.assertEqual('test_change_status', Label.objects.get(pk=1).name)

    def test_delete_label(self):
        response = self.client.get(reverse('labels:delete', args='2'))
        self.assertEqual(response.status_code, OK_CODE)
        response = self.client.post(reverse('labels:delete', args='2'))
        self.assertEqual(response.status_code, REDIRECT_CODE)

        with self.assertRaises(Label.DoesNotExist):
            Label.objects.get(pk=2)

    def test_delete_label_in_task(self):
        response = self.client.get(reverse('labels:delete', args='1'))
        self.assertEqual(response.status_code, OK_CODE)
        response = self.client.post(reverse('labels:delete', args='1'))
        self.assertEqual(response.status_code, REDIRECT_CODE)
        self.assertEqual('test_label_in_task', Label.objects.get(pk=1).name)
