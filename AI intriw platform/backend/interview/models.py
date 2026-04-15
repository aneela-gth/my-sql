from django.db import models

class InterviewResult(models.Model):
    student_name = models.CharField(max_length=100)
    score = models.IntegerField()
    feedback = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)