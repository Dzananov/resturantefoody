from django.db import models
from django.contrib.auth.models import User


GUESTS = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
)


TIME_FRAME = (
    ('16-17', '16-17'),
    ('17-18', '17-18'),
    ('18-19', '18-19'),
    ('19-20', '19-20'),
)


class Reservation(models.Model):
    costumer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="costumer_reservation")
    name = models.CharField(max_length=50)
    email = models.EmailField()
    guests = models.IntegerField(choices=GUESTS, default='2')
    time = models.IntegerField(choices=TIME_FRAME, default='17-18')
    date = models.DateField()

    class Meta:
        ordering = ('date', 'time')
        unique_together = ('guests', 'time', 'date')

    def __str__(self):
        return self.name
