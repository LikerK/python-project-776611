from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Status
from .forms import StatusForm
from django.utils.translation import gettext_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class StatusList(LoginRequiredMixin, ListView):
    model = Status
    login_url = 'login'
    template_name = 'statuses.html'
    context_object_name = 'statuses'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = gettext_lazy('Statuses')
        return context
    

class CreateStatus(LoginRequiredMixin, CreateView):
    model = Status
    form_class = StatusForm
    template_name = 'form.html'
    success_url = reverse_lazy('statuses')
    redirect_field_name = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = gettext_lazy('Statuses')
        context['button_text'] = gettext_lazy('Create')
        return context


class UpdateStatus(LoginRequiredMixin, UpdateView):
    model = Status
    form_class = StatusForm
    login_url = 'login'
    template_name = 'form.html'
    success_url = reverse_lazy('statuses:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = gettext_lazy('Statuses')
        context['button_text'] = gettext_lazy('Change')
        return context

class DeleteStatus(LoginRequiredMixin, DeleteView):
    model = Status
    template_name = 'delete.html'
    login_url = 'login'
    success_url = reverse_lazy('statuses:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = gettext_lazy('Statuses')
        context['button_text'] = gettext_lazy('Delete')
        context['text'] = gettext_lazy('Are you sure you want to delete')
        return context