from django.urls import path
from task_manager.labels.views import (
    LabelList,
    CreateLabel,
    UpdateLabel,
    DeleteLabel,
)

app_name = 'labels'

urlpatterns = [
    path('', LabelList.as_view(), name='list'),
    path('create/', CreateLabel.as_view(), name='create'),
    path('<int:pk>/update/', UpdateLabel.as_view(), name='change'),
    path('<int:pk>/delete/', DeleteLabel.as_view(), name='delete'),
]
