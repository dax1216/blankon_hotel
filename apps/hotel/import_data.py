import pandas as pd
from apps.hotel.models import Event
from django.conf import settings

csv_file_path = settings.BASE_DIR / 'datasets/data.csv'
df = pd.read_csv(csv_file_path)

# Iterate through the DataFrame and create model instances
for index, row in df.iterrows():
    Event.objects.create(
        hotel_id=row['hotel_id'],
        rpg_status=row['status'],
        room_id=row['room_reservation_id'],
        night_of_stay=row['night_of_stay'],
        timestamp=row['event_timestamp']
    )

print("CSV data has been loaded into the Django database.")