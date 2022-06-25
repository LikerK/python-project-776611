from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy


STATUS = 'statuses.html'
FORM = 'form.html'
DELETE = 'delete.html'
STATUSES_LIST = reverse_lazy('statuses:list')
CREATE_STATUS = gettext_lazy('Created status successfully')
CHANGE_STATUS = gettext_lazy('Update status successfully')
DELETE_STATUS = gettext_lazy('Delete status successfully')
ERROR_DELETE_STATUS = gettext_lazy("Can't remove status because it used")
CREATE_TEXT = gettext_lazy('Create')
CHANGE_TEXT = gettext_lazy('Change')
BUTTON_TEXT_DELETE = gettext_lazy('Yes, delete')
TITLE = 'title'
BUTTON_TEXT = 'button_text'
TEXT = 'text'
TEXT_CONTENT = gettext_lazy('Are you sure you want to delete')
CREATE_TITLE = gettext_lazy('Create status')
DELETE_TITLE = gettext_lazy('Delete status')
LIST_TITLE = gettext_lazy('Statuses')
CHANGE_TITLE = gettext_lazy('Change status')
