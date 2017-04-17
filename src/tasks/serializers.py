from rest_framework import serializers

from tasks.models import Task


class TaskSerializer(serializers.ModelSerialLizer):

    class Meta:
        model = Task
        field = '__all__'
