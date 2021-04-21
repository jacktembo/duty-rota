from django.contrib.auth.models import User
from django.db import models
from dutyrota.utils import *
from teachers.models import Teacher, Supervisor

from datetime import date


class School(models.Model):
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    logo = models.ImageField()
    headteacher = models.CharField(max_length=50)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    website = models.CharField(max_length=64, blank=True, null=True)
    facebook = models.URLField(max_length=255)
    twitter = models.URLField(max_length=255, blank=True, null=True)


class DutyRota(models.Model):
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
