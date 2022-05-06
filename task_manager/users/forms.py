from dataclasses import field
from django.contrib.auth.forms import UserCreationForm

from .models import User

class UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2',
        ]

