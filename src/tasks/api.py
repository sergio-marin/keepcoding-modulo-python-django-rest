from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from tasks.models import Task
from tasks.serializers import TaskSerializer, TaskListSerializer


class TaskViewSet(ModelViewSet):

    queryset = Task.objects.all()
    permission_classes = (IsAuthenticated, )

    def get_serializer_class(self):
        return TaskListSerializer if self.action == "list" else TaskSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)