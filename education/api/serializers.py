from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from education.models import *


class LessonSerializer(serializers.ModelSerializer):
    course = serializers.SlugRelatedField(slug_field='name', read_only=True)
    group = serializers.SlugRelatedField(slug_field='name', read_only=True)
    room = serializers.SlugRelatedField(slug_field='room_number', read_only=True)
    teacher = serializers.StringRelatedField(read_only=True)
    timetable = serializers.StringRelatedField(read_only=True)
    # lesson_type = serializers.SlugRelatedField(slug_field='name', read_only=True,)
    day = serializers.CharField(source='get_day_display', read_only=True)

    class Meta:
        model = Lesson
        exclude = ['id', 'even_week']

class CreateLessonSerializer(serializers.ModelSerializer):
    pass

class TimeTableSerializer(serializers.ModelSerializer):
    time_from = serializers.SlugRelatedField(read_only=True)
    time_until = serializers.SlugRelatedField(read_only=True)

    class Meta:
        model = Timetable
        exclude = ['id',]


class CreateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(min_length=8, write_only=True)

    def create(self, validated_data):
        user = User(email=validated_data['email'],)
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ('email', 'password',)
        extra_kwargs = {'password': {'write_only': True}}
