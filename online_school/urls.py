from online_school.apps import OnlineSchoolConfig
from rest_framework.routers import DefaultRouter
from online_school.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDeleteAPIView, PaymentCreateAPIView, PaymentListAPIView, PaymentDeleteAPIView
from django.urls import path


app_name = OnlineSchoolConfig.name
router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lessons/', LessonListAPIView.as_view(), name='lessons'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lesson/delete/<int:pk>/', LessonDeleteAPIView.as_view(), name='lesson_delete'),

    path('payment/create/', PaymentCreateAPIView.as_view(), name='payment_create'),
    path('payments/', PaymentListAPIView.as_view(), name='payments'),
    path('payment/delete/<int:pk>/', PaymentDeleteAPIView.as_view(), name='payment_delete')
              ] + router.urls
