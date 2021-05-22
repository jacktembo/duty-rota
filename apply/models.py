from django.db import models
from django.contrib.auth.models import User


class PersonalDetails(models.Model):
    """Personal details for each applicant. An applicant has to fill in 
    these details and save.

    Args:
        models ([type]): [description]

    Returns:
        [type]: [description]
    """
    # A user to which these personal details belong.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    portrait = models.ImageField(
        blank=True, null=True, upload_to="student-portraits")
    title = models.CharField(max_length=5)
    first_Name = models.CharField(max_length=20)
    other_Names = models.CharField(max_length=200, blank=True)
    last_Name = models.CharField(max_length=20)
    date_of_birth = models.DateField(default="2020-01-01")
    marital_Status = models.CharField(max_length=20)
    nationality = "Zambian"
    gender = models.CharField(max_length=10)
    NRC = models.CharField(max_length=12)
    passport = models.CharField(max_length=12, blank=True)
    copy_of_nrc = models.FileField(
        null=True, blank=True, upload_to="student-nrc")

    def __str__(self):
        return f"personal details for {self.first_Name}"

    class Meta:
        verbose_name_plural = "personal details"


class ContactDetails(models.Model):
    """ Contact details of a student"""
    # A user to which these contact details belong.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    alternate_Phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=64)
    postal_code = models.CharField(max_length=10)
    country = models.CharField(max_length=20)
    province = models.CharField(max_length=20)
    town = models.CharField(max_length=20)
    residential_Address = models.CharField(max_length=200)
    postal_address = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "contact details"

    def __str__(self):
        return f"contact details for {self.user}"


class NextOfKin(models.Model):
    """A student's next of kin to contact"""
    # A user to whom the Next of Kin belong.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    relationship = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=64)
    residential_Address = models.CharField(max_length=200)
    postal_Address = models.CharField(max_length=200)

    def __str__(self):
        return self.email


class PreviousSchool(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    last_school_attended = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    town = models.CharField(max_length=20)
    date_of_graduation = models.DateField()
    qualification_obtained = models.CharField(max_length=50)
    person_of_contact = models.CharField(max_length=200)

    def __str__(self):
        return self.last_school_attended


class Parent(models.Model):
    """A parent for each student."""
    # A student to which this Parent belongs.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_Name = models.CharField(max_length=22)
    middle_Name = models.CharField(max_length=22, blank=True, null=True)
    last_Name = models.CharField(max_length=22)
    email = models.EmailField(max_length=64)
    phone = models.CharField(max_length=14)
    NRC_Number = models.CharField(max_length=10)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.first_Name
