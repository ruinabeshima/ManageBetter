from django.urls import path
from . import views

urlpatterns = [
  path("", views.teacher_dashboard, name="teacher_dashboard"),
  path("logout/", views.logout_view, name="logout")
]