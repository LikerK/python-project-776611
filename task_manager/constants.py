from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy


INDEX = 'index.html'
FORM = 'form.html'
LOG_IN = gettext_lazy('You are logged in')
LOG_OUT = gettext_lazy('You are not logged in')
NEXT_PAGE_HOME = reverse_lazy('home')
LOGIN = gettext_lazy('Log in')
INPUT = gettext_lazy('Input')
TITLE = 'title'
BUTTON_TEXT = 'button_text'
