from django_filters import BooleanFilter, FilterSet, ModelChoiceFilter
from django.forms import CheckboxInput
from task_manager.labels.models import Label
from django.utils.translation import gettext_lazy
from task_manager.tasks.models import Task


class TaskFilter(FilterSet):
    labels = ModelChoiceFilter(
        queryset=Label.objects.all(),
        label=gettext_lazy('Label'),
    )
    own_tasks = BooleanFilter(
        field_name='author',
        label=gettext_lazy('Show own tasks'),
        method='filter_own_tasks',
        widget=CheckboxInput,
    )

    def filter_own_tasks(self, queryset, name, value):
        if value:
            return queryset.filter(author=self.request.user)
        return queryset

    class Meta(object):
        model = Task
        fields = [
            'status',
            'executor',
            'labels',
            'own_tasks',
        ]
