from django.db import models
from utils import *
from teachers.models import Teacher, Supervisor


class DutyRota(models.Model):
    """Duty Rota for a specific day"""
    name = models.CharField(max_length=200)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    Month = models.ForeignKey(Month, on_delete=models.CASCADE)
    # Week number in a term.
    week_number = models.ForeignKey(Week, on_delete=models.CASCADE)
    # The day of the week e.g Monday.
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    # Teachers on duty.
    teachers = models.ManyToManyField('Teachers On Duty', Teacher)
    supervisors = models.ManyToManyField('supervisors On Duty', Supervisor)
