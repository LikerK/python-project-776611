from django.urls import path
from task_manager.labels.views import (
    LabelList,
    CreateLabel,
    UpdateLabel,
    DeleteLabel,
)

app_name = 'labels'

urlpatterns = [
    path('labels/', LabelList.as_view(), name='list'),
    path('labels/create/', CreateLabel.as_view(), name='create'),
    path('labels/<int:pk>/update/', UpdateLabel.as_view(), name='change'),
    path('labels/<int:pk>/delete/', DeleteLabel.as_view(), name='delete'),
]
