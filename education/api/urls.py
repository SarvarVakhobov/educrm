from django.urls import path
from .views import *

urlpatterns = [
    path('rooms/', RoomListView.as_view(), name='rooms'),
    path('room-detail/<int:pk>/', RoomDetailView.as_view(), name='room_detail'),
    path('create-timetable/', CreateTimeTableView.as_view(), name='create_timetable '),
    path('lessons/', LessonView.as_view(), name='lessons'),
]