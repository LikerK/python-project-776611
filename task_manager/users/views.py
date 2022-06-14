from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import User
from task_manager.constants.templates import USER, FORM, DELETE
from task_manager.constants.success_urls import USERS_LIST, LOGIN
from task_manager.constants.contexts.users import (
    CREATE_TITLE, 
    DELETE_TITLE, 
    LIST_TITLE,
)
from task_manager.constants.contexts.common_constant import (
    CHANGE_TEXT, 
    CREATE_TEXT, 
    CHANGE_TEXT, 
    DELETE_TEXT, 
    TEXT, TITLE, 
    BUTTON_TEXT, 
    TEXT_CONTENT,
)
from task_manager.constants.success_messages import (
    CREATE_USER,
    CHANGE_USER,
    DELETE_USER,
) 
from django.contrib.auth import get_user_model
from .forms import UserForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.utils import CustomLoginRequiredMixin


User = get_user_model()



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
        context[BUTTON_TEXT] = CREATE_TEXT
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
        context[BUTTON_TEXT] = DELETE_TEXT
        context[TITLE] = DELETE_TITLE
        context[TEXT] = TEXT_CONTENT
        return context
