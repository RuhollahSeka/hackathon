from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from waste_management.serializers import UserCreateSerializer


class UserCreateView(CreateAPIView):
    serializer_class = UserCreateSerializer

    def create(self, request: Request, *args, **kwargs):
        username = request.POST.get('username')
        if User.objects.filter(username=username).first():
            return Response(status=status.HTTP_200_OK)
        return super().create(request, *args, **kwargs)
