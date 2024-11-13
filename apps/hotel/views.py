from rest_framework import generics
from .models import Event
from .serializers import EventSerializer
from .filters import EventFilter
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class EventView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = EventFilter
