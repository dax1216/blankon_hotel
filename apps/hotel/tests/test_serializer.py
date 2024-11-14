import pytest
from django.utils import timezone
from rest_framework.exceptions import ValidationError

from apps.hotel.models import Event, RPGStatus
from apps.hotel.serializers import EventSerializer


@pytest.mark.django_db
def test_event_serializer_valid():
    data = {
        "hotel_id": 1,
        "rpg_status": RPGStatus.BOOKING,
        "room_id": "101A",
        "night_of_stay": timezone.now().date(),
        "timestamp": timezone.now(),
    }
    event = Event.objects.create(**data)
    serializer = EventSerializer(data=data)
    assert serializer.is_valid()
    assert serializer.data["hotel_id"] == event.hotel_id
    assert serializer.data["rpg_status"] == event.rpg_status
    assert serializer.data["room_id"] == event.room_id


def test_event_serializer_invalid():
    data = {
        "hotel_id": "not an integer",  # Invalid type
        "rpg_status": RPGStatus.CANCELLATION,
        "room_id": "101A",
        "night_of_stay": "2024-11-14",  # Valid date
        "timestamp": "2024-11-14T00:00:00Z",  # Valid datetime
    }
    serializer = EventSerializer(data=data)
    with pytest.raises(ValidationError):
        serializer.is_valid(raise_exception=True)
