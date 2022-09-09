from django.shortcuts import render

from django.http import Http404
from rest_framework import authentication, generics, mixins, permissions
from rest_framework.response import Response
from classApp.models import Announcement, Assignment, Student, StudentClass, AssignmentSolution, Teacher
from . import serializers
# Create your views here.

class StudentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = serializers.StudentSerializer

class AnnouncementDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Announcement.objects.all()
    serializer_class = serializers.AnnouncementSerializer

class TeacherDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = serializers.TeacherSerializer

class AssignmentSolutionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AssignmentSolution.objects.all()
    serializer_class = serializers.AssignmentSolutionSerializer

class StudentClassDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentClass.objects.all()
    serializer_class = serializers.StudentClassSerializer

class AssignmentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Assignment.objects.all()
    serializer_class = serializers.AssignmentSerializer




class StudentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = serializers.StudentSerializer

class AnnouncementListCreateAPIView(generics.ListCreateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = serializers.AnnouncementSerializer

class TeacherListCreateAPIView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = serializers.TeacherSerializer

class AssignmentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Assignment.objects.all()
    serializer_class = serializers.AssignmentSerializer

class AssignmentSolutionListCreateAPIView(generics.ListCreateAPIView):
    queryset = AssignmentSolution.objects.all()
    serializer_class = serializers.AssignmentSerializer

class StudentClassListCreateAPIView(generics.ListCreateAPIView):
    queryset = StudentClass.objects.all()
    serializer_class = serializers.StudentClassSerializer