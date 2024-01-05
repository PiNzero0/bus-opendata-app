# Generated by Django 3.2.23 on 2023-12-26 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agency_id', models.CharField(max_length=255)),
                ('agency_name', models.CharField(max_length=255)),
                ('agency_url', models.CharField(max_length=255)),
                ('agency_timezone', models.CharField(max_length=255)),
                ('agency_lang', models.CharField(max_length=255)),
                ('agency_phone', models.CharField(max_length=255)),
                ('agency_fare_url', models.CharField(max_length=255)),
                ('agency_email', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Agencyjp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agency_id', models.CharField(max_length=255)),
                ('agency_name', models.CharField(max_length=255)),
                ('agency_url', models.CharField(max_length=255)),
                ('agency_timezone', models.CharField(max_length=255)),
                ('agency_lang', models.CharField(max_length=255)),
                ('agency_phone', models.CharField(max_length=255)),
                ('agency_fare_url', models.CharField(max_length=255)),
                ('agency_email', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_id', models.CharField(max_length=255)),
                ('monday', models.IntegerField()),
                ('tuesday', models.IntegerField()),
                ('wednesday', models.IntegerField()),
                ('thursday', models.IntegerField()),
                ('friday', models.IntegerField()),
                ('saturday', models.IntegerField()),
                ('sunday', models.IntegerField()),
                ('start_date', models.CharField(max_length=255)),
                ('end_date', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Calendar_Dates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_id', models.CharField(max_length=255)),
                ('date', models.CharField(max_length=255)),
                ('exception_type', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Fare_Attributes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fare_id', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('currency_type', models.CharField(max_length=255)),
                ('payment_method', models.IntegerField()),
                ('transfers', models.IntegerField()),
                ('transfer_duration', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Fare_Rules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fare_id', models.CharField(max_length=255)),
                ('route_id', models.CharField(max_length=255)),
                ('origin_id', models.CharField(max_length=255)),
                ('destination_id', models.CharField(max_length=255)),
                ('contains_id', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='FeedInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feed_publisher_name', models.CharField(max_length=255)),
                ('feed_publisher_url', models.CharField(max_length=255)),
                ('feed_lang', models.CharField(max_length=255)),
                ('feed_start_date', models.CharField(max_length=255)),
                ('feed_end_date', models.CharField(max_length=255)),
                ('feed_version', models.CharField(max_length=255)),
                ('feed_contact_email', models.CharField(max_length=255)),
                ('feed_contact_url', models.CharField(max_length=255)),
                ('feed_contact_phone', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Frequencies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trip_id', models.CharField(max_length=255)),
                ('start_time', models.CharField(max_length=255)),
                ('end_time', models.CharField(max_length=255)),
                ('headway_secs', models.IntegerField()),
                ('exact_times', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Office_jp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('office_id', models.CharField(max_length=255)),
                ('office_name', models.CharField(max_length=255)),
                ('office_url', models.CharField(max_length=255)),
                ('office_phone', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Route_jp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route_id', models.CharField(max_length=255)),
                ('route_update_date', models.CharField(max_length=255)),
                ('origin_stop', models.CharField(max_length=255)),
                ('via_stop', models.CharField(max_length=255)),
                ('destination_stop', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Routes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route_id', models.CharField(max_length=255)),
                ('agency_id', models.CharField(max_length=255)),
                ('route_short_name', models.CharField(max_length=255)),
                ('route_long_name', models.CharField(max_length=255)),
                ('route_desc', models.CharField(max_length=255)),
                ('route_type', models.IntegerField()),
                ('route_url', models.CharField(max_length=255)),
                ('route_color', models.CharField(max_length=255)),
                ('route_text_color', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Shapes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shape_id', models.CharField(max_length=255)),
                ('shape_pt_lat', models.FloatField()),
                ('shape_pt_lon', models.FloatField()),
                ('shape_pt_sequence', models.IntegerField()),
                ('shape_dist_traveled', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Stop_Times',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trip_id', models.CharField(max_length=255)),
                ('arrival_time', models.CharField(max_length=255)),
                ('departure_time', models.CharField(max_length=255)),
                ('stop_id', models.CharField(max_length=255)),
                ('stop_sequence', models.IntegerField()),
                ('stop_headsign', models.CharField(max_length=255)),
                ('pickup_type', models.IntegerField()),
                ('drop_off_type', models.IntegerField()),
                ('shape_dist_traveled', models.FloatField()),
                ('timepoint', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Stops',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stop_id', models.CharField(max_length=255)),
                ('stop_code', models.CharField(max_length=255)),
                ('stop_name', models.CharField(max_length=255)),
                ('stop_desc', models.CharField(max_length=255)),
                ('stop_lat', models.FloatField()),
                ('stop_lon', models.FloatField()),
                ('zone_id', models.CharField(max_length=255)),
                ('stop_url', models.CharField(max_length=255)),
                ('location_type', models.IntegerField(default=0, null=True)),
                ('parent_station', models.CharField(max_length=255)),
                ('wheelchair_boarding', models.IntegerField(null=True)),
                ('platform_code', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Transfers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_stop_id', models.CharField(max_length=255)),
                ('to_stop_id', models.CharField(max_length=255)),
                ('transfer_type', models.IntegerField()),
                ('min_transfer_time', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Trips',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route_id', models.CharField(max_length=255)),
                ('service_id', models.CharField(max_length=255)),
                ('trip_id', models.CharField(max_length=255)),
                ('trip_headsign', models.CharField(max_length=255)),
                ('trip_short_name', models.CharField(max_length=255)),
                ('direction_id', models.IntegerField()),
                ('block_id', models.CharField(max_length=255)),
                ('shape_id', models.CharField(max_length=255)),
                ('wheelchair_accessible', models.IntegerField()),
                ('bikes_allowed', models.IntegerField()),
                ('jp_trip_desc', models.CharField(max_length=255)),
                ('jp_trip_desc_symbol', models.CharField(max_length=255)),
                ('jp_office_id', models.CharField(max_length=255)),
            ],
        ),
    ]