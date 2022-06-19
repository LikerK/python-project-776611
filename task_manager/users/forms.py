from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import User


class UserForm(UserCreationForm):
    class Meta:
        user = get_user_model()
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2',
        ]
