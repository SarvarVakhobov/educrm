from django.urls import path
from .views import *

urlpatterns = [
    path('rooms/', RoomListView.as_view(), name='rooms'),
    path('update-room/<int:id>/', UpdateRoomView.as_view(), name='update_room'),
    path('create-room/', CreateRoomView.as_view(), name='create_room'),
]