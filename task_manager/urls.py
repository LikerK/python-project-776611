from django.urls import path, include
from task_manager.views import LoginUser, LogoutUser, Index
from django.contrib import admin

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutUser.as_view(), name='logout'),
    path('', include('task_manager.users.urls')),
    path('admin/', admin.site.urls),
    path('', include('task_manager.statuses.urls')),
    path('', include('task_manager.labels.urls')),
    path('', include('task_manager.tasks.urls')),
]
