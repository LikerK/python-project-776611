from django.views.generic import ListView, CreateView, UpdateView
from .models import Status
from .forms import StatusForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.mixins import CustomDeleteMixin
from task_manager.statuses.constants import (
    CREATE_STATUS,
    CHANGE_STATUS,
    DELETE_STATUS,
    ERROR_DELETE_STATUS,
    STATUS,
    FORM,
    DELETE,
    STATUSES_LIST,
    CREATE_TEXT,
    CHANGE_TEXT,
    BUTTON_TEXT,
    BUTTON_TEXT_DELETE,
    TITLE,
    TEXT,
    TEXT_CONTENT,
    CREATE_TITLE,
    DELETE_TITLE,
    LIST_TITLE,
    CHANGE_TITLE,
)


class StatusList(LoginRequiredMixin, ListView):
    model = Status
    template_name = STATUS
    context_object_name = 'statuses'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[TITLE] = LIST_TITLE
        return context


class CreateStatus(LoginRequiredMixin, SuccessMessageMixin, CreateView):
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
        context[TITLE] = CHANGE_TITLE
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
        context[BUTTON_TEXT] = BUTTON_TEXT_DELETE
        context[TEXT] = TEXT_CONTENT
        return context
