from django.shortcuts import render
from .models import Question, Choice, Submission

def course_details(request):
    questions = Question.objects.all()
    return render(request, 'course_details_bootstrap.html', {'questions': questions})

def mock_exam_result(request):
    # Dummy result for screenshot
    score = 85
    return render(request, 'mock_exam_result.html', {'score': score})
