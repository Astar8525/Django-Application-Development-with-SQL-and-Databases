from django.urls import path
from . import views

urlpatterns = [
    path('course-details/', views.course_details, name='course_details'),
    path('mock-exam-result/', views.mock_exam_result, name='mock_exam_result'),
]
