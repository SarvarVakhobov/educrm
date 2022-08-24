from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404

from .serializers import *
from attendance.models import *


class AttendanceStudentDetailView(APIView):
    """
    Retrieve, update or delete a attandance instance.
    """
    def get_object(self, pk):
        try:
            return AttendanceStudents.objects.get(id=pk)
        except AttendanceStudents.DoesNotExist:
            raise http404

    def get(self, request, pk, format=None):
        atten = self.get_object(pk)
        serializer = AttendanceStudentSerializer(atten)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        atten = self.get_object(pk)
        serializer = AttendanceStudentSerializer(atten, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        atten = self.get_object(pk)
        atten.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AttendanceStudentView(APIView):
    """
    List all attendance, or create a new attandance.
    """
    def get(self, request, format=None):
        queryset = AttendanceStudents.objects.all()
        serializer = AttendanceStudentSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AttendanceStudentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

