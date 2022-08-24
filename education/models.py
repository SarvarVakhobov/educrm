from django.db import models
from django.utils.translation import gettext_lazy as __

# Create your models here
class Teacher(models.Model):
    first_name = models.CharField(__('first name'), max_length=40)
    last_name = models.CharField(__('last name'), max_length=40, null=True)

    def __str__(self):
        return f"{self.last_name}.{self.first_name[:1]}"
    

class Timetable(models.Model):
    time_from = models.TimeField(__('from'))
    time_until = models.TimeField(__('until'))

    def __str__(self):
        return f"{self.time_from} - {self.time_until}"
    
class Branch(models.Model):
    name = models.CharField(__("name of the branch"), max_length=255)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=80, blank=True, null=True)

    def __str__(self):
        return self.name

class LevelOfgroup(models.Model):
    name = models.CharField(max_length=80, blank=True, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(__('name of the group'), max_length=255)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='groups')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    level = models.ForeignKey(LevelOfgroup, on_delete=models.SET_NULL, null=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    date_activated = models.DateField(auto_now_add=True)
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.branch}"

class Student(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Room(models.Model):
    room_number = models.CharField(__('number of the room'), max_length=20)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.room_number)

# class LessonName(models.Model):
#     name = models.CharField(__("name of the lesson"), max_length=50)

#     def __str__(self):
#         return self.name

# class LessonType(models.Model):
#     name = models.CharField(__('type of lessons'), max_length=40)

#     def __str__(self):
#         return self.name

class Lesson(models.Model):
    # name = models.ForeignKey(LessonName, on_delete=models.CASCADE, related_name='lessons')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='lessons')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='lessons')
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='lessons')
    timetable = models.ForeignKey(Timetable, on_delete=models.CASCADE)
    # lesson_type = models.ForeignKey(LessonType, on_delete=models.CASCADE, related_name='lessons', default=1)
    even_week = models.BooleanField(__('even / odd week'), null=False)
    DAYS = (
        (1, __('Monday')),
        (2, __('Tuesday')),
        (3, __('Wednesday')),
        (4, __('Thursday')),
        (5, __('Friday')),
        (6, __('Saturday')),
        (7, __('Sunday')),
    )
    day = models.IntegerField(
        __('day of the week'), choices=DAYS)

    def __str__(self):
        return f'{self.course}, {self.day}'

    class Meta:
        ordering = ['day', 'timetable']
