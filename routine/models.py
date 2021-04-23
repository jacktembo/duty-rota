from django.contrib.auth.models import User
from django.db import models
from dutyrota.utils import *

from datetime import date

from django.db import models

class School(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    logo = models.ImageField(blank=True, null=True)
    headteacher = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    website = models.CharField(max_length=64, blank=True, null=True)
    facebook = models.URLField(max_length=255)
    twitter = models.URLField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Person(models.Model):
    """an abstract person where different persons type will inherit"""
    first_name = models.CharField(max_length=30)
    other_names = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
    nrc = models.CharField(max_length=12)
    birth_date = models.DateField()
    image_url = models.URLField(blank=True, null=True)
    picture = models.ImageField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Teacher(Person):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=14)
    department = models.CharField(max_length=50)
    email = models.EmailField(max_length=64)


class Supervisor(Teacher):
    pass




class DutyRota(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    """Duty Rota for a specific day"""
    name = models.CharField(max_length=200)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    date = models.DateField()
    # Teachers on duty.
    teachers = models.ManyToManyField(
        Teacher, related_name='+')

    supervisors = models.ManyToManyField(
        Supervisor, related_name='+')

    def __str__(self):
        # Date in format like Monday 10 January 2021.
        return self.date.strftime('%A. %w %A')

    class Meta:
        verbose_name_plural = 'Duty Rotas'


class Announcement(models.Model):
    """ Announcements to pupils or staff"""
    subject = models.CharField(max_length=200)
    body = models.TextField()
    target_audience = models.CharField(max_length=50)
    published_date = models.DateField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.subject


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
