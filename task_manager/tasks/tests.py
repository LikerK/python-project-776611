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

    