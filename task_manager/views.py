from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from django.utils.translation import gettext_lazy


class Index(TemplateView):
    template_name = "index.html"


class LoginUser(SuccessMessageMixin, LoginView):
    template_name = 'form.html'
    next_page = reverse_lazy('home')
    success_message = gettext_lazy('Perfect')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = gettext_lazy('Log in')
        context['button_text'] = gettext_lazy('Log in')
        context['value'] = 'login'
        return context


class LogoutUser(SuccessMessageMixin, LogoutView):
    next_page = reverse_lazy('home')
    def dispatch(self, request, *args, **kwargs):
        messages.add_message(request, messages.INFO, gettext_lazy('Succsess'))
        return super().dispatch(request, *args, **kwargs)
