from django.db import models
from django.contrib.auth.models import User


# STATUS = ((0, "avalible"), (1, "booked"))

# GUESTS = (
#     (1, '1'),
#     (2, '2'),
#     (3, '3'),
#     (4, '4'),
#     (5, '5'),
#     (6, '6'),
# )


# TIME_FRAME = (
#     (1, '16-17'),
#     (2, '17-18'),
#     (3, '18-19'),
#     (4, '19-20'),
# )





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
