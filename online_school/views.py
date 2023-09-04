from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter
from django_filters import rest_framework
from online_school.serializers import CourseSerializer, LessonSerializer, PaymentSerializer
from online_school.models import Course, Lesson, Payment


# Create your views here.
class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDeleteAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()


class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerializer


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [OrderingFilter, rest_framework.DjangoFilterBackend]
    ordering_fields = ['date_of_payment']
    filterset_fields = ['course', 'payment_method']


class PaymentDeleteAPIView(generics.DestroyAPIView):
    queryset = Payment.objects.all()
