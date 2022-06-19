from django import forms
from .models import Task
from django.utils.translation import gettext_lazy


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'name',
            'description',
            'author',
            'status',
            'executor',
            'label',
        ]
        label = {
            'name': gettext_lazy('Name'),
            'description': gettext_lazy('Description'),
            'author': gettext_lazy('Author'),
            'status': gettext_lazy('Status'),
            'executor': gettext_lazy('Executor'),
            'label': gettext_lazy('Label'),
        }
