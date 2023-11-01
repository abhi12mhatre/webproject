from django.db import models

from constants.Constants import PaymentType, PaymentMode
from user_manager.models import Record, Profile


# Create your models here.


class Package(Record):
    location = models.CharField(max_length=100)
    days = models.CharField(max_length=20)
    details = models.TextField()

    def __str__(self):
        return '{} - {}'.format(self.location, self.days)


class Customer(Profile, Record):
    aadhar_card = models.CharField(max_length=12)


class Tour(Record):
    package = models.ForeignKey(Package, null=True, blank=True, on_delete=models.SET_NULL)
    customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.SET_NULL)
    adult = models.PositiveSmallIntegerField(default=0)
    child = models.PositiveSmallIntegerField(default=0)
    date = models.DateField()
    cost = models.FloatField(default=0.0)
    amount = models.FloatField(default=0.0)
    discount = models.FloatField(default=0.0)


class Invoice(Record):
    date = models.DateField()
    tour = models.ForeignKey(Tour, null=True, blank=True, on_delete=models.SET_NULL)
    amount = models.FloatField(default=0.0)
    balance = models.FloatField(default=0.0)
    payment_mode = models.PositiveSmallIntegerField(default=PaymentMode.CASH, choices=PaymentMode.CHOICES)
    payment_type = models.PositiveSmallIntegerField(default=PaymentType.ADVANCE, choices=PaymentType.CHOICES)
