from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy


TEMPLATE_LABEL = 'labels.html'
TEMPLATE_FORM = 'form.html'
TEMPLATE_DELETE = 'delete.html'
LABELS_LIST = reverse_lazy('labels:list')
CREATE_LABEL = gettext_lazy('Created label successfully')
CHANGE_LABEL = gettext_lazy('Update label successfully')
DELETE_LABEL = gettext_lazy('Delete label successfully')
ERROR_DELETE_LABEL = gettext_lazy("Can't remove label because it used")
CREATE_TEXT = gettext_lazy('Create')
CHANGE_TEXT = gettext_lazy('Change')
BUTTON_TEXT_DELETE = gettext_lazy('Yes, delete')
TITLE = 'title'
BUTTON_TEXT = 'button_text'
TEXT = 'text'
TITLE_CREATE = gettext_lazy('Create label')
TITLE_CHANGE = gettext_lazy('Change label')
TITLE_DELETE = gettext_lazy('Delete label')
TITLE_LIST = gettext_lazy('Labels')
TEXT_CONTENT = gettext_lazy('Are you sure you want to delete')
