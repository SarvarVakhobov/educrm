from django.db import models
from education.models import Group, Student, Lesson

# Create your models here.
class AttendanceStudents(models.Model):
    STATUS = (
        ('at lesson', 'at lesson'),
        ('reasonable', 'reasonable'),
        ('not reasonable', 'not reasonable'),
    )
    holiday = models.BooleanField(default=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.group + str(self.date)


    