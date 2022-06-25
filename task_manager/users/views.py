from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import User
from task_manager.users.constans import (
    CREATE_TITLE,
    DELETE_TITLE,
    LIST_TITLE,
    BUTTON_TEXT_CREATE,
    USER,
    FORM,
    DELETE,
    USERS_LIST,
    CREATE_USER,
    CHANGE_USER,
    DELETE_USER,
    CHANGE_TEXT,
    BUTTON_TEXT_DELETE,
    TITLE,
    BUTTON_TEXT,
    TEXT,
    TEXT_CONTENT,
    LOGIN,
)
from .forms import UserForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.mixins import CustomLoginRequiredMixin


class UserList(ListView):
    model = User
    template_name = USER
    context_object_name = 'users'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[TITLE] = LIST_TITLE
        return context


class CreateUser(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserForm
    template_name = FORM
    success_url = LOGIN
    success_message = CREATE_USER

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[TITLE] = CREATE_TITLE
        context[BUTTON_TEXT] = BUTTON_TEXT_CREATE
        return context


class ChangeUser(
    CustomLoginRequiredMixin,
    SuccessMessageMixin,
    UpdateView,
    LoginRequiredMixin
):
    model = User
    form_class = UserForm
    template_name = FORM
    success_url = USERS_LIST
    success_message = CHANGE_USER

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[BUTTON_TEXT] = CHANGE_TEXT
        return context


class DeleteUser(
    CustomLoginRequiredMixin,
    SuccessMessageMixin,
    DeleteView,
):
    model = User
    template_name = DELETE
    success_url = USERS_LIST
    success_message = DELETE_USER

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[BUTTON_TEXT] = BUTTON_TEXT_DELETE
        context[TITLE] = DELETE_TITLE
        context[TEXT] = TEXT_CONTENT
        return context
