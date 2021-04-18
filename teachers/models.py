from django.db import models
from dutyrota.utils import Gender, Title


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

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Teacher(Person):
    phone_number = models.CharField(max_length=14)
    department = models.CharField(max_length=50)
    email = models.EmailField(max_length=64)


class Supervisor(Teacher):
    pass
