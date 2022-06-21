from django.urls import path
from task_manager.statuses.views import (
    StatusList,
    CreateStatus,
    UpdateStatus,
    DeleteStatus,
)

app_name = 'statuses'

urlpatterns = [
    path('', StatusList.as_view(), name='list'),
    path('create/', CreateStatus.as_view(), name='create'),
    path('<int:pk>/update/', UpdateStatus.as_view(), name='change'),
    path('<int:pk>/delete/', DeleteStatus.as_view(), name='delete'),
]
