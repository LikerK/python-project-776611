
from django.shortcuts import render
from django.utils.translation import gettext_lazy
from django.views.generic import ListView
from .models import User
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your views here.
class UserList(ListView):
    model = User
    tamplate_name = 'users.html'
    context_object_name = 'users'
    
