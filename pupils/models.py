from django.db import models


class LeavePermission(models.Model):
    """Permission for pupils to leave """
    pupil_name = models.CharField(max_length=50)
    pupil_id = models.CharField(max_length=20)
    reason = models.CharField(max_length=200)
    explanation = models.TextField()
    date_requested = models.DateTimeField(auto_now_add=True)
    duration = models.CharField(max_length=30)
