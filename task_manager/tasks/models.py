from django.db import models
from django.utils.translation import gettext_lazy
from task_manager.statuses.models import Status
from django.contrib.auth import get_user_model
from task_manager.labels.models import Label

User = get_user_model()
MAX_LENGTH = 100
MAX_LENGTH_OF_DESCRIPTION = 600


class Task(models.Model):
    name = models.CharField(
        max_length=MAX_LENGTH,
        unique=True,
        verbose_name=gettext_lazy('Name')
    )
    description = models.TextField(
        verbose_name=gettext_lazy('Description'),
        max_length=MAX_LENGTH_OF_DESCRIPTION,
        blank=True,
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        verbose_name=gettext_lazy('Status'),
        blank=False,
    )
    author = models.ForeignKey(
        User,
        null=False,
        on_delete=models.PROTECT,
        verbose_name=gettext_lazy('Auhtor'),
        related_name='tasks_author',
    )
    executor = models.ForeignKey(
        User,
        verbose_name=gettext_lazy('Executor'),
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name='tasks_executor',
    )
    labels = models.ManyToManyField(
        Label,
        verbose_name=gettext_lazy('Labels'),
        blank=True,
        related_name='tasks',
        through='LabelTaskIntermediate',
        through_fields=('task', 'label'),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=gettext_lazy('Date of create'),
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = gettext_lazy('Task')
        ordering = ['id']


class LabelTaskIntermediate(models.Model):
    label = models.ForeignKey(Label, on_delete=models.RESTRICT)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
