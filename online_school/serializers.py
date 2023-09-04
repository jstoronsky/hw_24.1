from rest_framework import serializers
from online_school.models import Course, Lesson, Payment


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    count_lessons = serializers.IntegerField(source='lesson_set.count')
    lessons = LessonSerializer(source='lesson_set', many=True)

    # @staticmethod
    # def get_count_lessons(obj):
    #     return obj.lesson_set.count()

    class Meta:
        model = Course
        fields = ['id', 'name', 'preview', 'description', 'count_lessons', 'lessons']


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'
