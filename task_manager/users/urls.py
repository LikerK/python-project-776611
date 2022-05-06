from django.urls import path
from task_manager.users.views import *

urlpatterns = [
    path('', UserList.as_view(), name='list'), #доделать список class UserList
    #path('create/', index), # CreateUser
    #path('<int:pk>/update/', index), #ChangeUser
    #path('<int:pk>/delete/', index) #DeleteUser

]