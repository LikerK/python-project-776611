from django.test import TestCase
from django.urls import reverse
from .models import Task
from task_manager.statuses.models import Status
from task_manager.users.models import User
from task_manager.labels.models import Label

# Create your tests here.
OK_CODE = 200
REDIRECT_CODE = 302


class TaskTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(
            username='user1',
            password='password1',
        )
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
        task.label.add(label_for_task)
        self.client.force_login(user)

    def test_task_list(self):
        response = self.client.get(reverse('tasks:list'))
        self.assertEqual(response.status_code, OK_CODE)
        self.assertQuerysetEqual(
            response.context_data['object_list'],
            Task.objects.all(),
            ordered=False,
        )

    def test_create_task(self):
        response = self.client.get(reverse('tasks:create'))
        self.assertEqual(response.status_code, OK_CODE)
        new_task = {
            'name': 'test_task2',
            'description': 'test',
            'status': Status.objects.get(pk=1),
        }
        response = self.client.post(reverse('tasks:create'), data=new_task, follow=True)  # noqa: E501
        second_task = Task.objects.get(pk=2)
        self.assertEqual(response.status_code, REDIRECT_CODE)
        print(Task.objects.all())
        self.assertEqual('test_task2', second_task.name)
        self.assertEqual('user1', second_task.author.name)

    def test_updage_task(self):
        response = self.client.get(reverse('tasks:change', args='1'))
        self.assertEqual(response.status_code, OK_CODE)
        response = self.client.post(reverse('tasks:change', args='1'), data={
            'name': 'test_change_task',
            'status': 'change_status_tasks',
            'label': 'change_label_task',
            },
        )
        first_task = self.client.get(Task.objects.get(pk=1))
        self.assertEqual(response.status_code, REDIRECT_CODE)
        self.assertEqual('test_change_task', first_task.name)
        self.assertEqual('change_status_tasks', first_task.status.name)
        self.assertEqual('change_label_task', first_task.label.name)

    def test_delete_task(self):
        response = self.client.get(reverse('tasks:delete', args='1'))
        self.assertEqual(response.status_code, OK_CODE)
        response = self.client.post(reverse('tasks:delete', args='1'))
        self.assertEqual(response.status_code, REDIRECT_CODE)

        with self.assertRaises(Label.DoesNotExist):
            Label.objects.get(pk=1)

    def test_delete_own_task(self):
        user2 = User.objects.create(
            username='user2',
            password='password',
        )
        Task.objects.create(
            name='task3',
            status=Status.objects.get(pk=1),
            author=user2
        )
        response = self.client.get(reverse('tasks:delete', args='2'))
        self.assertEqual(response.status_code, OK_CODE)
        response = self.client.post(reverse('tasks:delete', args='2'))
        self.assertEqual(response.status_code, REDIRECT_CODE)
        self.assertEqual('task3', Task.objects.get(pk=2).name)
