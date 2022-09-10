from django.urls import path
from . import views

urlpatterns = [
    path("students/", views.StudentListCreateAPIView.as_view(), name="students"),
    path("student/<int:pk>/", views.StudentDetailAPIView.as_view(), name="student-detail"),
    path("teachers/", views.TeacherListCreateAPIView.as_view(), name="teachers"),
    path("teacher/<int:pk>/", views.TeacherDetailAPIView.as_view(), name="teacher-detail"),
    path("announcements/", views.AnnouncementListCreateAPIView.as_view(), name="announcements"),
    path("announcement/<int:pk>/", views.AnnouncementDetailAPIView.as_view(), name="announcent-detail"),
    path("assignments/", views.AssignmentListCreateAPIView.as_view(), name="assignments"),
    path("assignment/<int:pk>", views.AssignmentDetailAPIView.as_view(), name="assignment-detail"),
    path("assignment_solutions/", views.AssignmentSolutionListCreateAPIView.as_view(), name="assignment-solutions"),
    path("assignment_solution/<int:pk>", views.AssignmentSolutionDetailAPIView.as_view(), name="assignment-solution-detail"),
    path("student_classes/", views.StudentClassListCreateAPIView.as_view(), name="student_classes"),
    path("student_class/<int:pk>", views.StudentClassDetailAPIView.as_view(), name="student-class")
]