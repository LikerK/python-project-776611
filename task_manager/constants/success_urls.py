from django.urls import reverse_lazy

USERS_LIST = reverse_lazy('users:list')
LABELS_LIST = reverse_lazy('labels:list')
STATUSES_LIST = reverse_lazy('statuses:list')
TASKS_LIST = reverse_lazy('tasks:list')
LOGIN = reverse_lazy('login')
