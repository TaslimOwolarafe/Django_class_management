from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.reverse import reverse
from classApp.models import Announcement, Assignment, Student, StudentClass, AssignmentSolution, Teacher

class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()

class StudentSerializer(ModelSerializer):
    user = UserPublicSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['user']
            
        

class TeacherSerializer(ModelSerializer):
    user = UserPublicSerializer(read_only=True)

    class Meta:
        model = User
        fields = [
            'user'
        ]

class StudentClassSerializer(ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='student-class', lookup_field='pk', read_only=True
    )
    class Meta:
        model = StudentClass
        fields = [
            'name', 'students', 'url'
        ]

        def get_students(self, StudentClass):
            students = []
            for student in StudentClass.students:
                students.append(f"{student.first_name} {student.last_name}")
            return students

class AssignmentSerializer(ModelSerializer):
    class Meta:
        model = Assignment
        fields = [
            'name', 'student_class', 'body', 'attachment',
            'teacher', 'date_given'
        ]

class AssignmentSolutionSerializer(ModelSerializer):
    class Meta:
        model = AssignmentSolution
        fields = [
            'student', 'assignment', 'solution', 
            'date_submitted', 'completed'
        ]

class AnnouncementSerializer(ModelSerializer):
    body = serializers.SerializerMethodField()
    class Meta:
        model = Announcement
        fields = [
            'title', 'body', 'student_class',
            'teacher', 'date_posted'
        ]

    def get_body(self, Announcement):
        return Announcement.body[:30]
