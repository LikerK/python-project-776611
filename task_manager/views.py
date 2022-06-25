from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.base import TemplateView
from django.contrib import messages
from task_manager.constants import (
    NEXT_PAGE_HOME,
    LOGIN,
    INPUT,
    INDEX,
    FORM,
    LOG_IN,
    LOG_OUT,
    TITLE,
    BUTTON_TEXT
)


class Index(TemplateView):
    template_name = INDEX


class LoginUser(SuccessMessageMixin, LoginView):
    template_name = FORM
    next_page = NEXT_PAGE_HOME
    success_message = LOG_IN

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[TITLE] = INPUT
        context[BUTTON_TEXT] = LOGIN
        return context


class LogoutUser(SuccessMessageMixin, LogoutView):
    next_page = NEXT_PAGE_HOME

    def dispatch(self, request, *args, **kwargs):
        messages.add_message(request, messages.INFO, LOG_OUT)
        return super().dispatch(request, *args, **kwargs)
