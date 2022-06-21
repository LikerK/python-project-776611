from django.urls import path
from task_manager.tasks.views import (
    TaskList,
    CreateTask,
    UpdateTask,
    DeleteTask,
    TaskDetails
)

app_name = 'tasks'

urlpatterns = [
    path('', TaskList.as_view(), name='list'),
    path('create/', CreateTask.as_view(), name='create'),
    path('<int:pk>/update/', UpdateTask.as_view(), name='change'),
    path('<int:pk>/delete/', DeleteTask.as_view(), name='delete'),
    path('<int:pk>/', TaskDetails.as_view(), name='details'),
]
