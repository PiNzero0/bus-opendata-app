# models.py

from django.db import models

class Agency(models.Model):
    agency_id = models.CharField(max_length=255)
    agency_name = models.CharField(max_length=255)
    agency_url = models.CharField(max_length=255)
    agency_timezone = models.CharField(max_length=255)
    agency_lang = models.CharField(max_length=255)
    agency_phone = models.CharField(max_length=255,null=True)
    agency_fare_url = models.CharField(max_length=255,null=True)
    agency_email = models.CharField(max_length=255,null=True)

class Agencyjp(models.Model):
    agency_id = models.CharField(max_length=255)
    agency_official_name = models.CharField(max_length=255, null=True)
    agency_zip_number = models.CharField(max_length=255, null = True)
    agency_address = models.CharField(max_length=255, null=True)
    agency_president_pos = models.CharField(max_length=255,null=True)
    agency_president_name = models.CharField(max_length=255,null=True)

class Stops(models.Model):
    stop_id = models.CharField(max_length=255)
    stop_code = models.CharField(max_length=255, null=True)
    stop_name = models.CharField(max_length=255, null=True)
    stop_desc = models.CharField(max_length=255, null=True)
    stop_lat = models.FloatField()
    stop_lon = models.FloatField()
    zone_id = models.CharField(max_length=255, null=True)
    stop_url = models.CharField(max_length=255, null=True)
    location_type = models.IntegerField(default=0, null=True)
    parent_station = models.CharField(max_length=255, null=True)
    wheelchair_boarding = models.IntegerField(null=True)
    platform_code = models.CharField(max_length=255, null=True)

class Routes(models.Model):
    route_id = models.CharField(max_length=255)
    agency_id = models.CharField(max_length=255)
    route_short_name = models.CharField(max_length=255, null=True)
    route_long_name = models.CharField(max_length=255, null=True)
    route_desc = models.CharField(max_length=255, null=True)
    route_type = models.IntegerField(null=True)
    route_url = models.CharField(max_length=255,null=True)
    route_color = models.CharField(max_length=255, null=True)
    route_text_color = models.CharField(max_length=255, null=True)


class Route_jp(models.Model):
    route_id = models.CharField(max_length=255)
    route_update_date = models.CharField(max_length=255, null=True)
    origin_stop = models.CharField(max_length=255, null=True)
    via_stop = models.CharField(max_length=255, null=True)
    destination_stop = models.CharField(max_length=255, null=True)

class Trips(models.Model):
    route_id = models.CharField(max_length=255)
    service_id = models.CharField(max_length=255)
    trip_id = models.CharField(max_length=255)
    trip_headsign = models.CharField(max_length=255, null=True)
    trip_short_name = models.CharField(max_length=255, null=True)
    direction_id = models.IntegerField(null=True)
    block_id = models.CharField(max_length=255, null=True)
    shape_id = models.CharField(max_length=255, null=True)
    jp_trip_desc = models.CharField(max_length=255, null=True)

class Office_jp(models.Model):
    office_id = models.CharField(max_length=255)
    office_name = models.CharField(max_length=255)
    office_url = models.CharField(max_length=255, null=True)
    office_phone = models.CharField(max_length=255, null=True)

class Stop_Times(models.Model):
    trip_id = models.CharField(max_length=255)
    arrival_time = models.CharField(max_length=255)
    departure_time = models.CharField(max_length=255)
    stop_id = models.CharField(max_length=255)
    stop_sequence = models.IntegerField()
    stop_headsign = models.CharField(max_length=255, null=True)
    pickup_type = models.IntegerField(null=True)
    drop_off_type = models.IntegerField(null=True)
    timepoint = models.IntegerField(null=True)

class Calendar(models.Model):
    service_id = models.CharField(max_length=255)
    monday = models.IntegerField()
    tuesday = models.IntegerField()
    wednesday = models.IntegerField()
    thursday = models.IntegerField()
    friday = models.IntegerField()
    saturday = models.IntegerField()
    sunday = models.IntegerField()
    start_date = models.CharField(max_length=255)
    end_date = models.CharField(max_length=255)

class Calendar_Dates(models.Model):
    service_id = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    exception_type = models.IntegerField()

class Fare_Attributes(models.Model):
    fare_id = models.CharField(max_length=255)
    price = models.FloatField(null=True,blank=True)
    currency_type = models.CharField(max_length=255)
    payment_method = models.IntegerField()
    transfers = models.IntegerField()
    transfer_duration = models.CharField(max_length=255, null=True,blank=True)

class Fare_Rules(models.Model):
    fare_id = models.CharField(max_length=255)
    route_id = models.CharField(max_length=255, null=True)
    origin_id = models.CharField(max_length=255, null=True)
    destination_id = models.CharField(max_length=255, null=True)

class Shapes(models.Model):
    shape_id = models.CharField(max_length=255)
    shape_pt_lat = models.FloatField()
    shape_pt_lon = models.FloatField()
    shape_pt_sequence = models.IntegerField()
class Frequencies(models.Model):
    trip_id = models.CharField(max_length=255)
    start_time = models.CharField(max_length=255)
    end_time = models.CharField(max_length=255)
    headway_secs = models.IntegerField()
    exact_times = models.IntegerField(null=True)

class Transfers(models.Model):
    from_stop_id = models.CharField(max_length=255)
    to_stop_id = models.CharField(max_length=255)
    transfer_type = models.IntegerField()
    min_transfer_time = models.IntegerField(null=True)

class Translations(models.Model):
    table_name = models.CharField(max_length=255)
    field_name = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    translation = models.CharField(max_length=255)
    trans_id = models.CharField(max_length=255)
    lang = models.CharField(max_length=255)
    record_id = models.CharField(max_length=255)
    record_sub_id = models.CharField(max_length=255)

class FeedInfo(models.Model):
    feed_publisher_name = models.CharField(max_length=255)
    feed_publisher_url = models.CharField(max_length=255)
    feed_lang = models.CharField(max_length=255)
    feed_start_date = models.CharField(max_length=255, null=True)
    feed_end_date = models.CharField(max_length=255, null=True)
    feed_version = models.CharField(max_length=255, null=True)
    