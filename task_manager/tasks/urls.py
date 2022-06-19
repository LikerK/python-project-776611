from django.urls import path
from task_manager.tasks.views import (
    TaskList,
    CreateTask,
    UpdateTask,
    DeleteTask,
)

app_name = 'tasks'

urlpatterns = [
    path('tasks', TaskList.as_view(), name='list'),
    path('tasks/create/', CreateTask.as_view(), name='create'),
    path('tasks/<int:pk>/update/', UpdateTask.as_view(), name='change'),
    path('tasks/<int:pk>/delete/', DeleteTask.as_view(), name='delete'),
]
