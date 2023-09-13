from rest_framework import serializers
from online_school.models import Course, Lesson, Payment, Subscription
from online_school.validators import VideoLinkValidator
from users.models import User


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [VideoLinkValidator(field='video_link')]


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['id', 'course', 'user', 'is_active']


class SubscriptionSerializerForList(serializers.ModelSerializer):
    course = serializers.SlugRelatedField('name', read_only=True)
    user = serializers.SlugRelatedField('email', read_only=True)

    class Meta:
        model = Subscription
        fields = ['id', 'course', 'user', 'is_active']


class CourseSerializer(serializers.ModelSerializer):
    count_lessons = serializers.IntegerField(source='lesson_set.count', read_only=True)
    lessons = LessonSerializer(source='lesson_set', many=True, read_only=True)

    subscribed_users = serializers.SerializerMethodField()

    # @staticmethod
    # def get_count_lessons(obj):
    #     return obj.lesson_set.count()

    @staticmethod
    def get_subscribed_users(obj):
        queryset = obj.subscriptions.filter(is_active=True)
        serializer = SubscriptionSerializer(instance=queryset, many=True, read_only=True)
        return serializer.data

    class Meta:
        model = Course
        fields = ['id', 'name', 'preview', 'description', 'added_by', 'count_lessons', 'lessons', 'subscribed_users']


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'



