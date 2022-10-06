from django.db import models
from django.contrib.auth.models import User


class Table(models.Model):
    TABLE_SEATS = (
        ('Two', '2 SEATS'),
        ('Four', '4 SEATS'),
        ('Eight', '8 SEATS'),
    )
    number = models.IntegerField()
    seats = models.CharField(max_length=5, choices=TABLE_SEATS)

    def __str__(self):
        return f'Table number {self.number} for maximum {self.seats} costumers.'


class Reservation(models.Model):
    costumer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="costumer_reservation")
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    arriving_time = models.DateTimeField()
    leaving_time = models.DateTimeField()

    def __str__(self):
        return f'{self.costumer} had reserved  {self.table} table on {self.arriving_time} and is leaving {self.leaving_time}'
