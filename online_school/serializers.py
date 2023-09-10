from rest_framework import serializers
from online_school.models import Course, Lesson, Payment
from users.models import User


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    count_lessons = serializers.IntegerField(source='lesson_set.count', read_only=True)
    lessons = LessonSerializer(source='lesson_set', many=True, read_only=True)

    # @staticmethod
    # def get_count_lessons(obj):
    #     return obj.lesson_set.count()

    class Meta:
        model = Course
        fields = ['id', 'name', 'preview', 'description', 'added_by', 'count_lessons', 'lessons']


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'


class UserPaymentsSerializer(serializers.ModelSerializer):
    payments = PaymentSerializer(source='payment_set', many=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'city', 'phone_number', 'payments']
