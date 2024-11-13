from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('hotel_id', 'rpg_status', 'room_id', 'timestamp', 'night_of_stay')
        model = Event