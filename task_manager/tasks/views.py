from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from .models import Task
from django.contrib import messages
from django.shortcuts import redirect
from task_manager.users.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TaskForm
from task_manager.tasks.constants import (
    TEXT,
    TEXT_CONTENT,
    TITLE,
    BUTTON_TEXT,
    CREATE_TEXT,
    CHANGE_TEXT,
    BUTTON_TEXT_DELETE,
    TASK,
    FORM,
    DELETE,
    TASKS_LIST,
    CREATE_TASK,
    CHANGE_TASK,
    DELETE_TASK,
    ERROR_DELETE_TASK,
    CREATE_TITLE,
    DELETE_TITLE,
    CHANGE_TITLE,
    TASK_TITLE,
    SHOW,
    TASK_DETAILS_TITLE,
    TASK_DETAILS,
    LABEL,
)
from django.contrib.messages.views import SuccessMessageMixin
from django_filters.views import FilterView
from .filters import TaskFilter


class TaskList(LoginRequiredMixin, FilterView):
    model = Task
    template_name = TASK
    context_object_name = 'tasks'
    filterset_class = TaskFilter

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[TITLE] = TASK_TITLE
        context[BUTTON_TEXT] = SHOW
        return context


class TaskDetails(SuccessMessageMixin, LoginRequiredMixin, DetailView):
    model = Task
    template_name = TASK_DETAILS
    context_object_name = 'task_details'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[TITLE] = TASK_DETAILS_TITLE
        context[LABEL] = self.get_object().labels.all()
        return context


class CreateTask(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = FORM
    success_url = TASKS_LIST
    success_message = CREATE_TASK

    def form_valid(self, form):
        """Set author of task as active user."""
        form.instance.author = User.objects.get(pk=self.request.user.pk)
        return super().form_valid(form)

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


class DeleteTask(
    LoginRequiredMixin,
    SuccessMessageMixin,
    DeleteView,
):
    model = Task
    template_name = DELETE
    success_url = TASKS_LIST
    success_message = DELETE_TASK
    error_message = ERROR_DELETE_TASK
    redirect_url = TASKS_LIST

    def get(self, request, *args, **kwargs):
        """Delete a task only if the user is its creator"""
        if request.user != self.get_object().author:
            messages.error(
                self.request, self.error_message,
            )
            return redirect('tasks:list')
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[TITLE] = DELETE_TITLE
        context[BUTTON_TEXT] = BUTTON_TEXT_DELETE
        context[TEXT] = TEXT_CONTENT
        return context
