from django.urls import path
from .views import TaskList, TaskDetail,TaskCreate,TaskUpdate

urlpatterns = [
    path('', TaskList.as_view(), name='taskslist'),
    path('task/<int:pk>', TaskDetail.as_view(), name='task_detail'),
    path('task-create', TaskCreate.as_view(), name='task_create'),
    path('task-update/<int:pk>', TaskUpdate.as_view(), name='task_update'),
]
