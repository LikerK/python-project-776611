from django.views.generic import CreateView, UpdateView
from .models import Task
from task_manager.constants.templates import TASK, FORM, DELETE
from task_manager.constants.success_urls import TASKS_LIST
from django.contrib.auth.mixins import LoginRequiredMixin
from task_manager.utils import CustomLoginRequiredMixin
from .forms import TaskForm
from task_manager.constants.contexts.common_constant import (
    TEXT,
    TEXT_CONTENT,
    TITLE,
    BUTTON_TEXT,
    CREATE_TEXT,
    CHANGE_TEXT,
    DELETE_TEXT,
)
from task_manager.constants.success_messages import (
    CREATE_TASK,
    CHANGE_TASK,
    DELETE_TASK,
    ERROR_DELETE_TASK,
)
from task_manager.constants.contexts.tasks import (
    CREATE_TITLE,
    LIST_TITLE,
    DELETE_TITLE,
    CHANGE_TITLE,
    SHOW,
)
from django.contrib.messages.views import SuccessMessageMixin
from django_filters.views import FilterView
from .filters import TaskFilter
from task_manager.utils import CustomDeleteMixin


class TaskList(LoginRequiredMixin, FilterView):
    model = Task
    template_name = TASK
    context_object_name = 'tasks'
    filterset_class = TaskFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[TITLE] = LIST_TITLE
        context[BUTTON_TEXT] = SHOW
        return context


class CreateTask(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = FORM
    success_url = TASKS_LIST
    success_message = CREATE_TASK

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[TITLE] = CREATE_TITLE
        context[BUTTON_TEXT] = CREATE_TEXT
        return context


class UpdateTask(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = FORM
    success_url = TASKS_LIST
    success_message = CHANGE_TASK

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[TITLE] = CHANGE_TITLE
        context[BUTTON_TEXT] = CHANGE_TEXT
        return context


class DeleteTask(CustomLoginRequiredMixin, CustomDeleteMixin):
    model = Task
    template_name = DELETE
    success_url = TASKS_LIST
    success_message = DELETE_TASK
    deletion_error_message = ERROR_DELETE_TASK
    redirect_url = TASKS_LIST

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[TITLE] = DELETE_TITLE
        context[BUTTON_TEXT] = DELETE_TEXT
        context[TEXT] = TEXT_CONTENT
        return context
