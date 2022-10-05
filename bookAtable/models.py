from django.db import models
from django.conf import settings


class Table(models.Model):
    TABLE_SEATS = (
        ('Two', '2 SEATS'),
        ('Four', '4 SEATS'),
        ('Eight', '8 SEATS'),
    )
    number = models.IntegerField()
    seats = models.CharField(max_length=5, choices=TABLE_SEATS)

    def __str__(self):
        return f'{self.number} at a {self.seats} seated table.'


class Reservation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date_time = models.DateTimeField()

    def __str__(self):
        return f'{self.user} had reserved a {self.table} seated table on {self.date_time}'