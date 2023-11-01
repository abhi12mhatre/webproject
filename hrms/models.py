from django.db import models

from constants.Constants import Department, Position
from user_manager.models import Profile, Record


# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Employee(Profile, Record):
    company = models.ForeignKey(Company, null=True, blank=True, on_delete=models.SET_NULL)
    code = models.CharField(max_length=50, unique=True)
    department = models.PositiveSmallIntegerField(default=Department.ADMIN, choices=Department.CHOICES)
    position = models.PositiveSmallIntegerField(default=Position.INTERN, choices=Position.CHOICES)
    manager = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='e_manager')
    joining_date = models.DateField()
    leaving_date = models.DateField(null=True, blank=True)
    available_leaves = models.FloatField(default=0.0)
    salary = models.FloatField(default=0.0, name='emp_salary')


class LeaveTracker(Record):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    duration = models.FloatField(default=0.0)
    unpaid_leave_count = models.FloatField(default=0.0)


class Salary(Record):
    date = models.DateField()
    employee = models.ForeignKey(Employee, null=True, blank=True, on_delete=models.SET_NULL)
    base_amount = models.FloatField(default=0.0)
    deduction = models.FloatField(default=0.0)
    pay_amount = models.FloatField(default=0.0)
