from django.urls import path
from .views import *

urlpatterns = [
    path('attendance/', AttendanceStudentView.as_view(), name='attendance'),
    path('attendance-detail/<int:pk>/', AttendanceStudentDetailView.as_view(), name='attendance_detail'),
]