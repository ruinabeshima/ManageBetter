from django.db import models
from users.models import User

class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    code = models.CharField(max_length=10, unique=True) 
    teacher = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'teacher'}, 
        related_name='courses_taught'
    )
    students = models.ManyToManyField(
        User,
        limit_choices_to={'role': 'student'},  
        related_name='courses_enrolled',
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

