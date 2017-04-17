from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import UserSerializer


class UsersAPI(APIView):

    def get(self, request):
        """
        Returns a list of system users
        :param request: HttpResuest
        :return: HttpResponse
        """
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)