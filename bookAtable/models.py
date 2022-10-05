from django.db import models


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
