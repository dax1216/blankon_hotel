from django.db import models


class RPGStatus(models.TextChoices):
    BOOKING = "1", "Booking"
    CANCELLATION = "2", "Cancellation"


class Event(models.Model):
    hotel_id = models.IntegerField()
    rpg_status = models.CharField(max_length=5, choices=RPGStatus.choices, default=RPGStatus.BOOKING)
    room_id = models.CharField(max_length=100)
    night_of_stay = models.DateField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"{self.hotel_id} - {self.room_id} - {self.night_of_stay}"