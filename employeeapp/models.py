from django.db import models
from django.utils import timezone

class Employee(models.Model):
    GENDER_OPTIONS = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
        ('Unspecified', 'Unspecified'),
    ]

    given_name = models.CharField(max_length=100, blank=True, null=True)
    family_name = models.CharField(max_length=100, blank=True, null=True)
    work_email = models.EmailField(unique=True, null=True, blank=True)

    mobile = models.CharField(max_length=15, blank=True, null=True)
    sex = models.CharField(max_length=20, choices=GENDER_OPTIONS, default='Unspecified')
    home_address = models.TextField(blank=True, null=True)
    account_number = models.CharField(max_length=30, blank=True, null=True)
    role = models.CharField(max_length=100, default='Employee')
    base_pay = models.FloatField(default=0.0)
    completed_projects = models.IntegerField(default=0)
    years_employed = models.IntegerField(default=0, help_text="How long the person has worked here (in years)")
    joined_on = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.given_name or ''} {self.family_name or ''}".strip()
