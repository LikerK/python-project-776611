from django.urls import path
from task_manager.statuses.views import (
    StatusList,
    CreateStatus,
    UpdateStatus,
    DeleteStatus,
)

app_name = 'statuses'

urlpatterns = [
    path('statuses/', StatusList.as_view(), name='list'),
    path('statuses/create/', CreateStatus.as_view(), name='create'),
    path('statuses/<int:pk>/update/', UpdateStatus.as_view(), name='change'),
    path('statuses/<int:pk>/delete/', DeleteStatus.as_view(), name='delete'),
]
