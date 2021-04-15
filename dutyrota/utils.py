
""" utility classes and functions that will be used throughout the
project
"""
from django.db import models


class Year(models.Model):
    """Represents the year for the duty rota"""
    year = models.IntegerField(default=2021)

    def __str__(self):
        return self.year


class Term(models.Model):
    """Represents a school term e.g term 1, term 2 and term 3."""
    term = models.CharField(max_length=10)
    number_of_weeks = 13

    def _str__(self):
        return self.term


class Month(models.Model):
    """
    Represents the month of the year
    """
    month = models.CharField(max_length=20)
    number_of_days = models.IntegerField(default=30)

    def _str__(self):
        return self.month


class Week(models.Model):
    """Represents the week number in a term. There are typically 13 weeks 
    in a standard term"""
    week = models.IntegerField()

    def __str__(self):
        return self.week


class Day(models.Model):
    """Represents a day in a week. E.g Monday"""
    day = models.CharField(max_length=20)

    def _str__(self):
        return self.day


class Gender(models.Model):
    gender = models.CharField(max_length=15)

    def __str__(self):
        return self.gender


class Title(models.Model):
    title = models.CharField(max_length=5)

    def _str__(self):
        return self.title
