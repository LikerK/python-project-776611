from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy


TASK = 'tasks.html'
FORM = 'form.html'
DELETE = 'delete.html'
TASKS_LIST = reverse_lazy('tasks:list')
CREATE_TASK = gettext_lazy('Created task successfully')
CHANGE_TASK = gettext_lazy('Update task successfully')
DELETE_TASK = gettext_lazy('Delete task successfully')
ERROR_DELETE_TASK = gettext_lazy('A task can only be deleted by its author')
CREATE_TEXT = gettext_lazy('Create')
CHANGE_TEXT = gettext_lazy('Change')
BUTTON_TEXT_DELETE = gettext_lazy('Yes, delete')
TITLE = 'title'
BUTTON_TEXT = 'button_text'
TEXT = 'text'
TEXT_CONTENT = gettext_lazy('Are you sure you want to delete')
CREATE_TITLE = gettext_lazy('Create task')
DELETE_TITLE = gettext_lazy('Delete task')
CHANGE_TITLE = gettext_lazy('Change task')
TASK_TITLE = gettext_lazy('Tasks')
SHOW = gettext_lazy('Show')
TASK_DETAILS_TITLE = gettext_lazy('Task details')
TASK_DETAILS = 'task_details.html'
LABEL = 'label'
