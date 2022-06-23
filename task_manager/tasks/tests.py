from django.test import TestCase
from django.urls import reverse
from .models import Task
from task_manager.statuses.models import Status
from task_manager.users.models import User
from task_manager.labels.models import Label


OK_CODE = 200
REDIRECT_CODE = 302


class TaskTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(
            first_name='Djon',
            last_name='Snow',
            username='user1',
            password='password1',
        )
        user.save()
        status_for_task = Status.objects.create(
            name='test_status_in_task'
        )
        label_for_task = Label.objects.create(
            name='test_label_in_task',
        )
        task = Task.objects.create(
            name='test_task',
            status=status_for_task,
            author=user,
        )
        task.labels.add(label_for_task)

    def test_task_list(self):
        self.client.force_login(User.objects.get(pk=1))
        response = self.client.get(reverse('tasks:list'))
        self.assertEqual(response.status_code, OK_CODE)
        self.assertQuerysetEqual(
            response.context_data['object_list'],
            Task.objects.all(),
            ordered=False,
        )

    def test_create_task(self):
        self.client.force_login(User.objects.get(pk=1))
        response = self.client.get(reverse('tasks:create'))
        self.assertEqual(response.status_code, OK_CODE)
        self.assertTemplateUsed(
            response, template_name='form.html'
        )
        respone = self.client.post(reverse('tasks:create'), data={
            'name': 'test_task2',
            'description': 'test',
            'status': 1,
            'labels': 1,
        },
        )
        task2 = Task.objects.get(pk=2)
        self.assertEqual(respone.status_code, REDIRECT_CODE)
        self.assertEqual('user1', task2.author.username)
        self.assertEqual('test_task2', task2.name)
        self.assertEqual('test', task2.description)

    def test_update_task(self):
        self.client.force_login(User.objects.get(pk=1))
        Status.objects.create(name='status_for_update')
        response = self.client.get(reverse('tasks:change', args='1'))
        self.assertEqual(response.status_code, OK_CODE)
        response = self.client.post(reverse('tasks:change', args='1'), data={
            'name': 'test_update',
            'description': 'test',
            'status': 2,
            'labels': 1,
            }
        )
        self.assertEqual(response.status_code, REDIRECT_CODE)
        self.assertEqual('test_update', Task.objects.get(pk=1).name)
        self.assertEqual(
            'status_for_update',
            Task.objects.get(pk=1).status.name
        )

    def test_delete_task(self):
        self.client.force_login(User.objects.get(pk=1))
        response = self.client.get(reverse('tasks:delete', args='1'))
        self.assertEqual(response.status_code, OK_CODE)
        response = self.client.post(reverse('tasks:delete', args='1'))
        self.assertEqual(response.status_code, REDIRECT_CODE)
        with self.assertRaises(Task.DoesNotExist):
            Task.objects.get(pk=1)

    def test_delete_not_own_task(self):
        self.client.force_login(User.objects.get(pk=1))
        user2 = User.objects.create(
            first_name='Ariya',
            last_name='Stark',
            username='user2',
            password='password2',
        )
        Task.objects.create(
            name='test_delete',
            description='test2',
            status=Status.objects.get(pk=1),
            author=user2
        )
        response = self.client.get(reverse('tasks:delete', args='2'))
        self.assertEqual(response.status_code, REDIRECT_CODE)
