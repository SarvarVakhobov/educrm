from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404

from .serializers import *
from education.models import *

class CreateTimeTableView(APIView):
    def post(self, request):
        serializer = TimeTableSerializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RoomDetailView(APIView):
    """
    Retrieve, update or delete a room instance.
    """
    def get_object(self, pk):
        try:
            return Room.objects.get(id=pk)
        except Room.DoesNotExist:
            raise http404

    def get(self, request, pk, format=None):
        room = self.get_object(pk)
        serializer = RoomSerializer(room)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        room = self.get_object(pk)
        serializer = RoomSerializer(room, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        room = self.get_object(pk)
        room.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class RoomListView(APIView):
    """
    List all rooms, or create a new room.
    """
    def get(self, request, format=None):
        queryset = Room.objects.all()
        serializer = RoomSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LessonView(APIView):
    def get(self, request):
        even_week = request.data.get('even_week')
        group_name = request.data.get('group_name')
        lessons = Lesson.objects.filter(
            even_week=even_week,
            group__name=group_name,
        )
        serializer = LessonSerializer(lessons, many=True)
        return Response(serializer.data)


class TeacherView(APIView):
    def get(self, request):
        last_name = request.data.get('last_name')
        lessons = Lesson.objects.filter(
            teacher__last_name='last_name',
        )
        serializer = LessonSerializer(lessons, many=True)
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    serializer = CreateUserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response({'message': 'user successfully registered'},
                    status=status.HTTP_201_CREATED)