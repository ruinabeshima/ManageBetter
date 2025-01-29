from django.db import models
from courses.models import Course
from users.models import User

class Grading(models.Model):
    student = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'student'},
        related_name='grades'
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='grades')
    grade = models.CharField(max_length=2)  # Example: A, B, C
    feedback = models.TextField(blank=True)

    def __str__(self):
        return f"{self.student.username} - {self.course.name} - {self.grade}"
