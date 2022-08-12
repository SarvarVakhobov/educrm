from django.db import models
from education.models import Branch, Group, Room

# Create your models here.
class Marking_system(models.Model):
    mark_name = models.CharField(max_length=10)
    mark_from = models.IntegerField(default=100)
    mark_upto = models.IntegerField(blank=True)

    def __str__(self):
        return self.mark_name

class Exams_list(models.Model):
    exam_name = models.CharField(max_length=50, blank=True)
    info = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return self.exam_name

class Exams(models.Model):
    exam = models.ForeignKey(Exams_list, on_delete=models.CASCADE, blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    exam_day = models.DateField(blank=True, null=True)
    time_from = models.TimeField(blank=True, null=True)
    room_num = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)
    score_max = models.IntegerField(default=100)
    required_score = models.IntegerField(default=0)
    
    def __str__(self):
        return self.exam_name + self.group

class Marking(models.Model):
    exam = models.ForeignKey(Exams, on_delete=models.CASCADE, blank=True, null=True)
    

    def __str__(self):
        return self.exam