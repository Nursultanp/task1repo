

from django.urls import path
from .views import *
urlpatterns = [
    path('tasks/', TaskListCreateAPIView.as_view(), name='task_list_create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyAPIView.as_view(), name='task_detail'),
    path('tags/', TagListCreateAPIView.as_view(), name='tag_list_create'),
    path('tags/<int:pk>/', TagRetrieveUpdateDestroyAPIView.as_view(), name='tag_detail'),
]

