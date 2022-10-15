from django.db import models
from django.contrib.auth.models import User


STATUS = ((0, "avalible"), (1, "booked"))

GUESTS = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
)


TIME_FRAME = (
    (1, '16-17'),
    (2, '17-18'),
    (3, '18-19'),
    (4, '19-20'),
)


class Table(models.Model):
    number = models.IntegerField(choices=GUESTS, default=2)
    time = models.IntegerField(choices=TIME_FRAME, default=2)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.status


class Reservation(models.Model):
    costumer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="costumer_reservation")
    name = models.CharField(max_length=50)
    email = models.EmailField()
    guests = models.IntegerField(choices=GUESTS)
    time = models.IntegerField(choices=TIME_FRAME, default=2)
    date = models.DateField()
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ('date', 'time')
        unique_together = ('guests', 'time', 'date')

    def __str__(self):
        return self.name
