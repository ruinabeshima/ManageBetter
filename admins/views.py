from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def admin_dashboard(request):

    if request.user.role != 'admin':
        return HttpResponseForbidden("You are not authorized to view this page.")

    return render(request, 'admins/dashboard.html')
