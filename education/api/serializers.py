from rest_framework import serializers
from rest_framework.validators import UniqueValidator, UniqueTogetherValidator

from education.models import *
from user.models import CustomUser


class TimeTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timetable
        fields = "__all__"

    def create(self, validated_data):
        return Timetable.objects.create(**validated_data)

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=Room.objects.all(),
                fields=['room_number', 'branch']
            )
        ]
        

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

    def create(self, validated_data):
        return Lesson(**validated_data)

    def update(self, instance, validated_data):
        instance.course = validated_data.get('course', instance.course)
        instance.group = validated_data.get('group', instance.group)
        instance.room = validated_data.get('room', instance.room)
        instance.teacher = validated_data.get('teacher', instance.teacher)
        instance.timetable = validated_data.get('timetable', instance.timetable)
        instance.day = validated_data.get('day', instance.day)
        instance.save()
        return instance
    


class CreateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=CustomUser.objects.all())]
            )
    password = serializers.CharField(min_length=8, write_only=True)

    def create(self, validated_data):
        user = User(email=validated_data['email'],)
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = CustomUser
        fields = ('email', 'password',)
        extra_kwargs = {'password': {'write_only': True}}
