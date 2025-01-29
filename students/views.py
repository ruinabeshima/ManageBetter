from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import HttpResponseForbidden, HttpResponseRedirect
from courses.models import Course
from django.urls import reverse


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def student_dashboard(request):

    if request.user.role != 'student':
        return HttpResponseForbidden("You are not authorized to view this page.")

  
    courses = Course.objects.filter(students=request.user)

    return render(request, 'students/dashboard.html', {
        'courses': courses
    })