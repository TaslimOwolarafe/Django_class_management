from django.contrib import admin
from . models import Student, StudentClass, Teacher, Announcement, Assignment, AssignmentSolution


admin.site.register(Student)
admin.site.register(StudentClass)
admin.site.register(Teacher)
admin.site.register(Announcement)
admin.site.register(Assignment)
admin.site.register(AssignmentSolution)
