from django.utils.translation import gettext_lazy


ERROR_MESSAGE = gettext_lazy('You are denied access to this action')


#  home
LOG_IN = gettext_lazy('You are logged in')
LOG_OUT = gettext_lazy('You are not logged in')
#  users
CREATE_USER = gettext_lazy('Created user successfully')
CHANGE_USER = gettext_lazy('Update user successfully')
DELETE_USER = gettext_lazy('Delete user successfully')

#  tasks
CREATE_TASK = gettext_lazy('Created task successfully')
CHANGE_TASK = gettext_lazy('Update task successfully')
DELETE_TASK = gettext_lazy('Delete task successfully')
ERROR_DELETE_TASK = gettext_lazy('A task can only be deleted by its author')

#  statuses
CREATE_STATUS = gettext_lazy('Created status successfully')
CHANGE_STATUS = gettext_lazy('Update status successfully')
DELETE_STATUS = gettext_lazy('Delete status successfully')
ERROR_DELETE_STATUS = gettext_lazy("Can't remove status because it used")

#  labels
CREATE_LABEL = gettext_lazy('Created label successfully')
CHANGE_LABEL = gettext_lazy('Update label successfully')
DELETE_LABEL = gettext_lazy('Delete label successfully')
ERROR_DELETE_LABEL = gettext_lazy("Can't remove label because it used")
