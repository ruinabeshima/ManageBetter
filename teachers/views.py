from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponseRedirect
from courses.models import Course
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def teacher_dashboard(request):
    
    if request.user.role != 'teacher':
        return HttpResponseForbidden("You are not authorized to view this page.")

    
    courses = Course.objects.filter(teacher=request.user)

    return render(request, 'teachers/dashboard.html', {
        'courses': courses
    })
