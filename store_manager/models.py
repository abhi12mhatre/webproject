from django.db import models

from constants.Constants import ClientType, OrderType, OrderStatus
from user_manager.models import Profile, Record


# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name


class Client(Profile, Record):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    delivery_address = models.TextField(null=True, blank=True)
    type = models.PositiveSmallIntegerField(default=ClientType.CUSTOMER, choices=ClientType.CHOICES)

    def __str__(self):
        return self.store.name


class Product(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Order(Record):
    date = models.DateField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    rate = models.FloatField(default=0.0)
    amount = models.FloatField(default=0.0)
    discount = models.FloatField(default=0.0)
    type = models.PositiveSmallIntegerField(default=OrderType.OUTWARD, choices=OrderType.CHOICES)
    order_status = models.PositiveSmallIntegerField(default=OrderStatus.NEW, choices=OrderStatus.CHOICES)


class Invoice(Record):
    date = models.DateField()
    order = models.ForeignKey(Order, null=True, blank=True, on_delete=models.SET_NULL)
    amount = models.FloatField(default=0.0)
    balance = models.FloatField(default=0.0)
    is_paid = models.BooleanField(default=False)


class Stock(Record):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)



