from django.urls import path
from task_manager.users.views import *

app_name = 'users'

urlpatterns = [
    path('users/', UserList.as_view(), name='list'), #доделать список class UserList
    path('create/', CreateUser.as_view(), name='create'), # CreateUser
    path('<int:pk>/update/', ChangeUser.as_view(), name='change'), #ChangeUser
    path('<int:pk>/delete/', DeleteUser.as_view(), name='delete') #DeleteUser

]