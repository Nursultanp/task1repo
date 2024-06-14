from rest_framework import generics, pagination
from .models import Task, Tag
from .serializers import TaskSerializer, TagSerializer
from rest_framework.permissions import IsAuthenticated

class TaskPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class TaskListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    pagination_class = TaskPagination

class TagListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = TaskPagination