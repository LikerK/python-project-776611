from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy


USER = 'users.html'
FORM = 'form.html'
DELETE = 'delete.html'
USERS_LIST = reverse_lazy('users:list')
LOGIN = reverse_lazy('login')
CREATE_USER = gettext_lazy('Created user successfully')
CHANGE_USER = gettext_lazy('Update user successfully')
DELETE_USER = gettext_lazy('Delete user successfully')
CREATE_TEXT = gettext_lazy('Create')
CHANGE_TEXT = gettext_lazy('Change')
BUTTON_TEXT_DELETE = gettext_lazy('Yes, delete')
TITLE = 'title'
BUTTON_TEXT = 'button_text'
TEXT = 'text'
TEXT_CONTENT = gettext_lazy('Are you sure you want to delete')
CREATE_TITLE = gettext_lazy('Registration')
DELETE_TITLE = gettext_lazy('Delete User')
LIST_TITLE = gettext_lazy('Users')
BUTTON_TEXT_CREATE = gettext_lazy('Register')
