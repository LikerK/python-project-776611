from task_manager.labels.constants import (
    TEMPLATE_LABEL,
    TEMPLATE_FORM,
    TEMPLATE_DELETE,
    LABELS_LIST,
    CHANGE_LABEL,
    DELETE_LABEL,
    CREATE_LABEL,
    ERROR_DELETE_LABEL,
    CREATE_TEXT,
    CHANGE_TEXT,
    BUTTON_TEXT,
    BUTTON_TEXT_DELETE,
    TITLE,
    TEXT,
    TEXT_CONTENT,
    TITLE_CREATE,
    TITLE_CHANGE,
    TITLE_DELETE,
    TITLE_LIST,
)
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, CreateView, UpdateView
from .models import Label
from .forms import LabelForm
from django.contrib.auth.mixins import LoginRequiredMixin
from task_manager.mixins import CustomDeleteMixin


# Create your views here.
class LabelList(LoginRequiredMixin, ListView):
    model = Label
    template_name = TEMPLATE_LABEL
    context_object_name = 'labels'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[TITLE] = TITLE_LIST
        return context


class CreateLabel(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Label
    form_class = LabelForm
    template_name = TEMPLATE_FORM
    success_url = LABELS_LIST
    success_message = CREATE_LABEL

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[TITLE] = TITLE_CREATE
        context[BUTTON_TEXT] = CREATE_TEXT
        return context


class UpdateLabel(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Label
    form_class = LabelForm
    template_name = TEMPLATE_FORM
    success_url = LABELS_LIST
    success_message = CHANGE_LABEL

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[TITLE] = TITLE_CHANGE
        context[BUTTON_TEXT] = CHANGE_TEXT
        return context


class DeleteLabel(CustomDeleteMixin):
    model = Label
    template_name = TEMPLATE_DELETE
    success_url = LABELS_LIST
    success_message = DELETE_LABEL
    deletion_error_message = ERROR_DELETE_LABEL

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[TITLE] = TITLE_DELETE
        context[BUTTON_TEXT] = BUTTON_TEXT_DELETE
        context[TEXT] = TEXT_CONTENT
        return context
