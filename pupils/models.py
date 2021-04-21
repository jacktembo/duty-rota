from django.db import models

from routine.models import School


class LeavePermission(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    """Permission for pupils to leave """
    pupil_name = models.CharField(max_length=50)
    pupil_email = models.EmailField(max_length=64)
    pupil_id = models.CharField(max_length=20)
    pupil_phone = models.CharField(max_length=10)
    reason = models.CharField(max_length=200)
    explanation = models.TextField()
    date_requested = models.DateTimeField(auto_now_add=True)
    date_leaving = models.DateField()
    time_leaving = models.TimeField()
    date_back = models.DateField()

    def __str__(self):
        return f"From {self.pupil_name}"


class Grade(models.Model):
    grade = models.CharField(max_length=20)

    def __str__(self):
        return self.grade


class Pupil(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    pupil_id = models.CharField(max_length=20, primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateField()
    picture = models.ImageField(blank=True, null=True)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    parent_phone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
