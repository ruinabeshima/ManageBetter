from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse

# Default 
def index(request):
  return render(request, "users/homepage.html")

def admin_dashboard(request):
    return render(request, './admins/admin_dashboard.html')

def teacher_dashboard(request):
    return render(request, './teachers/teacher_dashboard.html')

def student_dashboard(request):
    return render(request, './students/student_dashboard.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)

            if request.user.is_student: 
                return HttpResponseRedirect('/students/')
            elif request.user.is_teacher: 
                return HttpResponseRedirect('/teachers')
            elif request.user.is_admin: 
                return HttpResponseRedirect('/admins')
            
        else:
            return render(request, "users/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "users/login.html")