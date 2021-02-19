from django.db import models
from django.utils import timezone

from user.models import User


class Ticket(models.Model):
    name = models.CharField(max_length=50)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    hash_code = models.CharField(max_length=50, unique=True)


class Order(models.Model):
    ticket = models.OneToOneField(to=Ticket, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    order_time = models.DateTimeField(default=timezone.now)
