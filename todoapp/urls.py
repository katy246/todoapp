from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('tasks/', views.TaskListView.as_view(), name='tasks'),
    path('task/<int:pk>',views.TaskDetailView.as_view(), name='task_detail'),
    path('task/create/', views.TaskCreate.as_view(), name='task_create'),
    path('task/<int:pk>/update/', views.TaskUpdate.as_view(), name='task_update'),
    path('task/<int:pk>/delete/', views.TaskDelete.as_view(), name='task_delete'),
]

