from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.reverse import reverse
from classApp.models import Announcement, Assignment, Student, StudentClass, AssignmentSolution, Teacher

class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    first_name = serializers.CharField()
    last_name = serializers.CharField()            
        

class StudentClassSerializer(ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='student-class', lookup_field='pk', read_only=True
    )
    students = serializers.StringRelatedField(many=True)
    teacher = serializers.StringRelatedField(many=False)

    class Meta:
        model = StudentClass
        fields = [
           'id', 'name', 'students', 'url', 'teacher'
        ]

class StudentSerializer(ModelSerializer):
    user = UserPublicSerializer(read_only=True)
    student_class = StudentClassSerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'user', 'student_class']

    # def to_representation(self, instance):
    #     return f"{instance.user.first_name} {instance.user.last_name}"

class TeacherSerializer(ModelSerializer):
    user = UserPublicSerializer(read_only=True)
    student_class = StudentClassSerializer(many=True)
    class Meta:
        model = User
        fields = [
            'id', 'user', 'student_class'
        ]

class AssignmentSerializer(ModelSerializer):
    class Meta:
        model = Assignment
        fields = [
            'id', 'name', 'student_class', 'body', 'attachment',
            'teacher', 'date_given'
        ]

class AssignmentSolutionSerializer(ModelSerializer):
    class Meta:
        model = AssignmentSolution
        fields = [
            'id', 'student', 'assignment', 'solution', 
            'date_submitted', 'completed'
        ]

class AnnouncementSerializer(ModelSerializer):
    body = serializers.SerializerMethodField()
    teacher = serializers.StringRelatedField(many=False)
    student_class = StudentClassSerializer(many=True)
    class Meta:
        model = Announcement
        fields = [
            'id', 'title', 'body', 'student_class',
            'teacher', 'date_posted'
        ]

    def get_body(self, Announcement):
        return Announcement.body[:30]
