import datetime
from bookAtable.models import Table, Reservation


def check_available(table, arriving_time, leaving_time):
    avail_list = []
    reservation_list = Reservation.objects.filter(table=table)
    for reservation in reservation_list:
        if reservation.arriving_time > leaving_time or reservation.leaving_time < arriving_time:
            avail_list.append(True)
        else:
            avail_list.append(False)
    return all(avail_list)
