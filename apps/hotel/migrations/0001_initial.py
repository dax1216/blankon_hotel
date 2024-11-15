# Generated by Django 5.1.3 on 2024-11-13 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_id', models.IntegerField()),
                ('rpg_status', models.CharField(choices=[('1', 'Booking'), ('2', 'Cancellation')], default='1', max_length=5)),
                ('room_id', models.CharField(max_length=100)),
                ('night_of_stay', models.DateField()),
                ('timestamp', models.DateTimeField()),
            ],
        ),
    ]
