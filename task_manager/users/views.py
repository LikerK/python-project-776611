from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import User
from django.contrib.auth import get_user_model
from django.contrib import messages
from .forms import UserForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy
from django.contrib.messages.views import SuccessMessageMixin

User = get_user_model()


class UserList(ListView):
    model = User
    template_name = 'users.html'
    context_object_name = 'users'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = gettext_lazy('Users')
        return context


class CreateUser(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'form.html'
    form_class = UserForm
    success_url = reverse_lazy('login')
    success_message = gettext_lazy("Created user successfully")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = gettext_lazy('Registration')
        context['button_text'] = gettext_lazy('Register')
        return context


class ChangeUser(UpdateView, LoginRequiredMixin):
    model = User
    template_name = 'form.html'
    form_class = UserForm
    success_url = reverse_lazy('users:list')
    unable_to_change_others_message = gettext_lazy(
        'You do not have permission to change another user.',
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['button_text'] = gettext_lazy('Change')
        return context
    
    def get(self, request, *args, **kwargs):
        if request.user != self.get_object():
            messages.error(
                self.request, self.unable_to_change_others_message,
            )
            return redirect('users:list')
        return super().get(request, *args, **kwargs)


class DeleteUser(DeleteView):
    model = User
    template_name = 'delete.html'
    success_url = reverse_lazy('users:list')
    error_message = gettext_lazy('Error')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['button_text'] = gettext_lazy('Delete')
        context['title'] = gettext_lazy('Delete User')
        context['text'] = gettext_lazy('Are you sure you want to delete')
        return context

    def get(self, request, *args, **kwargs):
        if request.user != self.get_object():
            messages.error(self.request, self.error_message)
            return redirect('users:list')
        return super().get(request, *args, **kwargs)




