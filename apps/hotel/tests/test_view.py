import pytest
from django.urls import reverse
from django.utils import timezone
from rest_framework.test import APIClient

from apps.hotel.models import Event, RPGStatus


@pytest.mark.django_db
def test_event_view_list():
    # Create some test events
    event_1 = Event.objects.create(
        hotel_id=1,
        rpg_status=RPGStatus.BOOKING,
        room_id="101A",
        night_of_stay="2024-11-10",
        timestamp=timezone.now(),
    )
    event_2 = Event.objects.create(
        hotel_id=1,
        rpg_status=RPGStatus.CANCELLATION,
        room_id="102B",
        night_of_stay="2024-11-12",
        timestamp=timezone.now(),
    )

    # Make an API request
    client = APIClient()
    url = reverse("events")  # Assuming this is the URL name for the view
    response = client.get(url)
    res = response.json()
    assert response.status_code == 200
    assert res["count"] == 2  # We created two events
    assert res["results"][0]["hotel_id"] == event_1.hotel_id
    assert res["results"][1]["hotel_id"] == event_2.hotel_id


@pytest.mark.django_db
def test_event_view_filter_by_night_of_stay():
    # Create test events
    Event.objects.create(
        hotel_id=1,
        rpg_status=RPGStatus.BOOKING,
        room_id="101A",
        night_of_stay="2024-11-10",
        timestamp=timezone.now(),
    )
    event_2 = Event.objects.create(
        hotel_id=1,
        rpg_status=RPGStatus.CANCELLATION,
        room_id="102B",
        night_of_stay="2024-11-12",
        timestamp=timezone.now(),
    )

    # Make a filtered request
    client = APIClient()
    url = reverse("events")  # Adjust URL name as necessary
    response = client.get(url, {"night_of_stay__gte": "2024-11-11"})
    res = response.json()
    assert response.status_code == 200
    assert res["count"] == 1  # Only one event matches the filter (event_2)
    assert res["results"][0]["hotel_id"] == event_2.hotel_id
