import pytest
from django.utils import timezone

from apps.hotel.models import Event, RPGStatus


@pytest.mark.django_db
def test_event_model_creation():
    event = Event.objects.create(
        hotel_id=1,
        rpg_status=RPGStatus.BOOKING,
        room_id="101",
        night_of_stay=timezone.now().date(),
        timestamp=timezone.now(),
    )
    assert event.hotel_id == 1
    assert event.rpg_status == RPGStatus.BOOKING
    assert event.room_id == "101"
    assert event.night_of_stay is not None
    assert event.timestamp is not None


@pytest.mark.django_db
def test_event_model_str():
    event = Event.objects.create(
        hotel_id=2,
        rpg_status=RPGStatus.CANCELLATION,
        room_id="102",
        night_of_stay=timezone.now().date(),
        timestamp=timezone.now(),
    )
    assert str(event) == "2 - 102 - {}".format(event.night_of_stay)
