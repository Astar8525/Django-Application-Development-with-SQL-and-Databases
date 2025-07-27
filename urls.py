from django.urls import path
from . import views

urlpatterns = [
    path('course/', views.course_details, name='course_details'),
]

