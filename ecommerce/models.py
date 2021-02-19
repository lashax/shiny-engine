from django.db import models


class Ticket(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    hash_code = models.CharField(max_length=50, unique=True)


class Order(models.Model):
    ticket = models.OneToOneField(to=Ticket, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

