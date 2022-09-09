from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class StudentClass(models.Model):
    name = models.CharField(max_length=225)
    students = models.ManyToManyField(Student, related_name='student_class')
    
    class Meta:
        verbose_name_plural = 'Student Classes'

    def __str__(self):
        return self.name
    
class Assignment(models.Model):
    name = models.CharField(max_length=225)
    student_class = models.ForeignKey(StudentClass, related_name='assignments', on_delete=models.SET_NULL, null=True)
    body = models.CharField(max_length=400, null=True)
    attachment = models.FileField(upload_to='assignments/',null=True)
    teacher = models.ForeignKey(Teacher, related_name='assignments', on_delete=models.SET_NULL, null=True)
    date_given = models.DateTimeField(auto_now_add=True)


class AssignmentSolution(models.Model):
    student = models.ForeignKey(Student, related_name='assignment_solutions', on_delete=models.SET_NULL, null=True)
    assignment = models.ForeignKey(Assignment, on_delete=models.SET_NULL, null=True)
    solution = models.FileField(upload_to='assignments_solutions/')
    date_submitted = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    @property
    def mark_completed(self):
        self.completed = True

class Announcement(models.Model):
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=300)
    student_class = models.ManyToManyField(StudentClass, related_name='announcemnts')
    teacher = models.ForeignKey(Teacher, related_name='announcements', on_delete=models.SET_NULL, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}: {self.body[:15]}, {self.teacher}"