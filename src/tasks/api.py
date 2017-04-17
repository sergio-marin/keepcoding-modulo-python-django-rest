from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from tasks.models import Task
from tasks.serializers import TaskSerializer


class TasksAPI(ListCreateAPIView):
    """
        Lists (GET) and creates (POST) tasks
    """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer