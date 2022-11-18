from django.db import models
from django.db.models import Model
import django.db.models.fields
from django.utils import timezone


# Create your models here.
class Farminformation(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)


class Workerspayment(models.Model):
    Name = models.CharField(max_length=255)
    DateTime = models.DateTimeField(default=timezone.now)
    Amount = models.DecimalField(max_digits=17, decimal_places=2, default=0.0)
    PaymentType = models.CharField(max_length=255)
    MobileNumber = models.BigIntegerField(10)
