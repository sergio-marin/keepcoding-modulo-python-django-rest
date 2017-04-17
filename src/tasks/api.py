from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from tasks.models import Task
from tasks.serializers import TaskSerializer


class TasksAPI(ListCreateAPIView):
    """
        Lists (GET) and creates (POST) tasks
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetailAPI(RetrieveUpdateDestroyAPIView):
    """
    Retrieves (GE), updates (PUT) and destroy (DELETE) a given task
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
