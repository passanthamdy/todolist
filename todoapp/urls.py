
from django.urls import path
from . import views

urlpatterns = [
    path('' , views.task_list, name='task_list'),
    path('<int:id>/', views.update_task, name = 'update_task'),
    path('delete_task/<int:id>/', views.delete_task, name= 'delete_task'),
]
