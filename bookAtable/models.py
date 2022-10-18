from django.db import models
from django.contrib.auth.models import User


class Reservation(models.Model):
    costumer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="costumer_reservation")
    name = models.CharField(max_length=50)
    email = models.EmailField()
    guests = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        ordering = ('date', 'time')
        unique_together = ('guests', 'time', 'date')

    def __str__(self):
        return self.name
