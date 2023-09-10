from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter
from django_filters import rest_framework
from rest_framework.permissions import IsAuthenticated
from online_school.serializers import CourseSerializer, LessonSerializer, PaymentSerializer, UserPaymentsSerializer
from online_school.models import Course, Lesson, Payment
from users.models import User
from online_school.permissions import IsModerator, IsSuperUser, IsOwner


# Create your views here.
class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def get_permissions(self):
        if self.action == 'list':
            self.permission_classes = [IsAuthenticated]

        elif self.action in ['retrieve', 'update', 'partial_update']:
            self.permission_classes = [IsAuthenticated,  IsModerator | IsSuperUser | IsOwner]

        elif self.action == 'create':
            self.permission_classes = [~IsModerator]

        elif self.action in ['create', 'destroy']:
            self.permission_classes = [IsAuthenticated, IsSuperUser]

        return super(CourseViewSet, self).get_permissions()


class LessonListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated,  IsModerator | IsSuperUser | IsOwner]
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, ~IsModerator]
    serializer_class = LessonSerializer


class LessonUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated,  IsModerator | IsSuperUser | IsOwner]
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, IsSuperUser]
    queryset = Lesson.objects.all()


class PaymentCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, IsSuperUser]
    serializer_class = PaymentSerializer


class PaymentListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated,  IsModerator | IsSuperUser]
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [OrderingFilter, rest_framework.DjangoFilterBackend]
    ordering_fields = ['date_of_payment']
    filterset_fields = ['course', 'payment_method']


class PaymentDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, IsSuperUser]
    queryset = Payment.objects.all()


class UserPaymentsListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated,  IsModerator | IsSuperUser]
    serializer_class = UserPaymentsSerializer
    queryset = User.objects.all()


class UserPaymentsRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated,  IsModerator | IsSuperUser]
    serializer_class = UserPaymentsSerializer
    queryset = User.objects.all()
