from django.db import models
from ..utils import *


class DutyRota(models.Model):
    name = models.CharField(max_length=200)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    Month = models.ForeignKey(Month, on_delete=models.CASCADE)
    week_number = models.IntegerField()  # Week number in a term.
    day = models.DateField()  # The day of the week e.g Monday.
    teachers = models.ManyToManyField('Teachers On Duty')  # Teachers on duty.
    supervisors = models.ManyToManyField('supervisors On Duty')
