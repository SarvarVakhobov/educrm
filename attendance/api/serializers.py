from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from attendance.models import *


class AttendanceStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceStudents()
        fields = "__all__"

    