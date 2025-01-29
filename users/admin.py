from django.contrib import admin
from .models import User
from courses.models import Course
from students.models import AssignmentSubmission
from teachers.models import Grading 
from admins.models import UserAudit 

# Register your models here.
admin.site.register(User)
admin.site.register(Course)
admin.site.register(AssignmentSubmission)
admin.site.register(Grading)
admin.site.register(UserAudit)