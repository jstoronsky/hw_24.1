from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from online_school.permissions import IsModerator, IsSuperUser
from users.models import User
from users.serializers import UsersSerializer, UserCreateSerializer


# Create your views here.
class UsersListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated,  IsModerator | IsSuperUser]
    serializer_class = UsersSerializer
    queryset = User.objects.all()


class UserCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, IsSuperUser]
    serializer_class = UserCreateSerializer


class UserUpdateAPIVIew(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated, IsSuperUser]
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()


class UsersRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated,  IsModerator | IsSuperUser]
    serializer_class = UsersSerializer
    queryset = User.objects.all()
