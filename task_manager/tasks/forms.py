from django import forms
from .models import Task
from django.utils.translation import gettext_lazy


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'name',
            'description',
            'status',
            'executor',
            'labels',
        ]
        label = {
            'name': gettext_lazy('Name'),
            'description': gettext_lazy('Description'),
            'status': gettext_lazy('Status'),
            'executor': gettext_lazy('Executor'),
            'label': gettext_lazy('Labels'),
        }
