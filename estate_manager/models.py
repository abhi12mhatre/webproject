from django.db import models

from user_manager.models import UserProfile, Record, Profile


# Create your models here.
class Estate(Record):
    owner = models.OneToOneField(UserProfile, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100)
    room_number = models.CharField(max_length=10)
    rent = models.FloatField(default=0.0)
    deposit = models.FloatField(default=0.0)
    details = models.TextField()
    address = models.TextField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Tenant(Profile, Record):
    estate = models.ForeignKey(Estate, null=True, blank=True, on_delete=models.SET_NULL)
    aadhar_card = models.CharField(max_length=12)
    agreement_start_date = models.DateField()
    agreement_end_date = models.DateField()


class Invoice(Record):
    estate = models.ForeignKey(Estate,  null=True, blank=True, on_delete=models.SET_NULL)
    tenant = models.ForeignKey(Tenant,  null=True, blank=True, on_delete=models.SET_NULL)
    from_date = models.DateField()
    to_date = models.DateField()
    amount = models.FloatField(default=0.0)
    balance = models.FloatField(default=0.0)
    is_paid = models.BooleanField(default=False)
