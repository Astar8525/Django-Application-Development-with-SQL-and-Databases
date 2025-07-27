from django.shortcuts import render
from models import Question

def course_details(request):
    questions = Question.objects.all()
    return render(request, 'course_details_bootstrap.html', {'questions': questions})

