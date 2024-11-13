from django_filters import rest_framework as filters
from .models import Event

class EventFilter(filters.FilterSet):
    night_of_stay__gte = filters.DateFilter(field_name='night_of_stay', lookup_expr='gte')
    night_of_stay__lte = filters.DateFilter(field_name='night_of_stay', lookup_expr='lte')
    timestamp__gte = filters.IsoDateTimeFilter(field_name='timestamp', lookup_expr='gte')
    timestamp__lte = filters.IsoDateTimeFilter(field_name='timestamp', lookup_expr='lte')

    class Meta:
        model = Event
        fields = [
            "hotel_id",
            "rpg_status",
            "room_id",
        ]