from django.urls import path 
from . import views

urlpatterns = [
  path("", views.index, name="index"),
  path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
  path('teacher_dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
  path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
  path('logout/', views.logout_view, name="logout"),
  path('login/', views.login_view, name="login")
]