from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.base import TemplateView
from django.contrib import messages
from task_manager.constants.templates import FORM, INDEX
from task_manager.constants.success_messages import LOG_IN, LOG_OUT
from task_manager.constants.contexts.common_constant import BUTTON_TEXT
from task_manager.constants.contexts.home import (
    NEXT_PAGE_HOME,
    LOGIN,
)
from task_manager.constants.contexts.common_constant import TITLE


class Index(TemplateView):
    template_name = INDEX


class LoginUser(SuccessMessageMixin, LoginView):
    template_name = FORM
    next_page = NEXT_PAGE_HOME
    success_message = LOG_IN

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[TITLE] = LOGIN
        context[BUTTON_TEXT] = LOGIN
        return context


class LogoutUser(SuccessMessageMixin, LogoutView):
    next_page = NEXT_PAGE_HOME

    def dispatch(self, request, *args, **kwargs):
        messages.add_message(request, messages.INFO, LOG_OUT)
        return super().dispatch(request, *args, **kwargs)
