from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from tasks.models import Task
from tasks.serializers import TaskSerializer, TaskListSerializer


class TasksAPI(ListCreateAPIView):
    """
    Lists (GET) and creates (POST) tasks
    """
    queryset = Task.objects.all()
    permission_classes = (IsAuthenticated, )

    def get_serializer_class(self):
        return TaskListSerializer if self.request.method == "GET" else TaskSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskDetailAPI(RetrieveUpdateDestroyAPIView):
    """
    Retrieves (GET), updates (PUT) and destroy (DELETE) a given task
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)