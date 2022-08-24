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
    status = models.CharField(max_length=30, choices=STATUS, default=STATUS[0][0])
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{str(self.student)} - {str(self.date)}"


    