from django.views.generic import ListView, CreateView, UpdateView
from .models import Status
from task_manager.constants.templates import STATUS, FORM, DELETE
from task_manager.constants.success_urls import STATUSES_LIST
from .forms import StatusForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.utils import CustomDeleteMixin
from task_manager.constants.success_messages import (
    CREATE_STATUS,
    CHANGE_STATUS,
    DELETE_STATUS,
    ERROR_DELETE_STATUS,
)
from task_manager.constants.contexts.statuses import (
    CREATE_TITLE,
    LIST_TITLE,
    DELETE_TITLE,
)
from task_manager.constants.contexts.common_constant import (
    TEXT,
    TEXT_CONTENT,
    TITLE,
    BUTTON_TEXT,
    CREATE_TEXT,
    CHANGE_TEXT,
    DELETE_TEXT,
)

# Create your views here.


class StatusList(LoginRequiredMixin, ListView):
    model = Status
    template_name = STATUS
    context_object_name = 'statuses'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[TITLE] = LIST_TITLE
        return context


class CreateStatus(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Status
    form_class = StatusForm
    template_name = FORM
    success_url = STATUSES_LIST
    success_message = CREATE_STATUS

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[TITLE] = CREATE_TITLE
        context[BUTTON_TEXT] = CREATE_TEXT
        return context


class UpdateStatus(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Status
    form_class = StatusForm
    template_name = FORM
    success_url = STATUSES_LIST
    success_message = CHANGE_STATUS

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[TITLE] = CHANGE_STATUS
        context[BUTTON_TEXT] = CHANGE_TEXT
        return context


class DeleteStatus(CustomDeleteMixin):
    model = Status
    template_name = DELETE
    success_url = STATUSES_LIST
    success_message = DELETE_STATUS
    deletion_error_message = ERROR_DELETE_STATUS

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[TITLE] = DELETE_TITLE
        context[BUTTON_TEXT] = DELETE_TEXT
        context[TEXT] = TEXT_CONTENT
        return context
