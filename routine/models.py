from django.db import models
from dutyrota.utils import *
from teachers.models import Teacher, Supervisor

from datetime import date


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
        #Date in format like Monday 10 January 2021.
        return self.date.strftime('%A %B %w %Y')

    class Meta:
        verbose_name_plural = 'Duty Rotas'
