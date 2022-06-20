from django.urls import path
from task_manager.users.views import (
    UserList,
    CreateUser,
    ChangeUser,
    DeleteUser,
)

app_name = 'users'

urlpatterns = [
    path('users/', UserList.as_view(), name='list'),
    path('users/create/', CreateUser.as_view(), name='create'),
    path('<int:pk>/update/', ChangeUser.as_view(), name='change'),
    path('<int:pk>/delete/', DeleteUser.as_view(), name='delete'),
]
