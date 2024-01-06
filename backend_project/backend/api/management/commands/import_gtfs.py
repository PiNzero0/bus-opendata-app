import csv
from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError
from api.models import *
import time

class Command(BaseCommand):
    help = 'Import GTFS data into the database'
    registrant = 'admin'
    retry = 10

    def handle(self, *args, **options):
        registrant, _ = Registrant.objects.get_or_create(name=self.registrant)
        no_calendar, _ = Calendar.objects.get_or_create(service_id='no_calendar', monday=0, tuesday=0, wednesday=0, thursday=0, friday=0, saturday=0, sunday=0, start_date='00000000', end_date='00000000', registrant=registrant)
        no_fair_attributes, _ = Fare_Attributes.objects.get_or_create(fare_id='no_fare_attributes', price=0, currency_type='JPY', payment_method=0, transfers=0, transfer_duration=0, registrant=registrant)

        # Agency テーブルのインポート
        with open('/backend/api/gtfs_data/agency.txt', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                Agency.objects.create(
                    agency_id=row['agency_id'],
                    agency_name=row['agency_name'],
                    agency_url=row['agency_url'],
                    agency_timezone=row['agency_timezone'],
                    agency_lang=row['agency_lang'],
                    agency_phone=row['agency_phone'],
                    agency_fare_url=row['agency_fare_url'],
                    agency_email=row['agency_email'],
                    registrant=registrant
                )
        
        # Calendar テーブルのインポート
        with open('/backend/api/gtfs_data/calendar.txt', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                Calendar.objects.create(
                    service_id=row['service_id'],
                    monday=row['monday'],
                    tuesday=row['tuesday'],
                    wednesday=row['wednesday'],
                    thursday=row['thursday'],
                    friday=row['friday'],
                    saturday=row['saturday'],
                    sunday=row['sunday'],
                    start_date=row['start_date'],
                    end_date=row['end_date'],
                    registrant=registrant
                )

        # CalendarDates テーブルのインポート
        with open('/backend/api/gtfs_data/calendar_dates.txt', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    calendar_obj = Calendar.objects.get(service_id=row['service_id'], registrant=registrant)
                except Calendar.DoesNotExist:
                    calendar_obj = no_calendar
                    
                Calendar_Dates.objects.create(
                    service_id=row['service_id'],
                    date=row['date'],
                    exception_type=row['exception_type'],
                    registrant=registrant,
                    calendar_obj=calendar_obj
                )
               
        # FareAttributes テーブルのインポート
        with open('/backend/api/gtfs_data/fare_attributes.txt', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                Fare_Attributes.objects.create(
                    fare_id=row['fare_id'],
                    price=row['price'],
                    currency_type=row['currency_type'],
                    payment_method=row['payment_method'],
                    transfers=row['transfers'],
                    transfer_duration=row['transfer_duration'],
                    registrant=registrant
                )

        # feed_info テーブルのインポート
        with open('/backend/api/gtfs_data/feed_info.txt', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                Feed_Info.objects.create(
                    feed_publisher_name=row['feed_publisher_name'],
                    feed_publisher_url=row['feed_publisher_url'],
                    feed_lang=row['feed_lang'],
                    feed_start_date=row['feed_start_date'],
                    feed_end_date=row['feed_end_date'],
                    feed_version=row['feed_version'],
                    registrant=registrant
                )
        
        # Routes テーブルのインポート
        with open('/backend/api/gtfs_data/routes.txt', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                agency_obj = Agency.objects.get(agency_id=row['agency_id'], registrant=registrant)
                Routes.objects.create(
                    route_id=row['route_id'],
                    agency_id=row['agency_id'],
                    route_short_name=row['route_short_name'],
                    route_long_name=row['route_long_name'],
                    route_desc=row['route_desc'],
                    route_type=row['route_type'],
#                    route_url=row['route_url'],
                    route_color=row['route_color'],
                    route_text_color=row['route_text_color'],
                    registrant=registrant,
                    agency_obj=agency_obj
                )

        # Shapes テーブルのインポート
        with open('/backend/api/gtfs_data/shapes.txt', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                Shapes.objects.create(
                    shape_id=row['shape_id'],
                    shape_pt_lat=row['shape_pt_lat'],
                    shape_pt_lon=row['shape_pt_lon'],
                    shape_pt_sequence=row['shape_pt_sequence'],
                    registrant=registrant
                )

        # Trips テーブルのインポート
        with open('/backend/api/gtfs_data/trips.txt', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # 'direction_id' の値が浮動小数点数である場合、整数に変換して利用
                direction_id_str = row['direction_id']
                direction_id = int(float(direction_id_str)) if direction_id_str.replace('.', '').isdigit() else None

                route_obj = Routes.objects.get(route_id=row['route_id'], registrant=registrant)
                try:
                    service_obj = Calendar.objects.get(service_id=row['service_id'], registrant=registrant)
                except Calendar.DoesNotExist:
                    service_obj = no_calendar
#                jp_office_obj = Office_jp.objects.filter(jp_office_id=row['jp_office_id'], registrant=registrant).first()

                trips = Trips.objects.create(
                    route_id=row['route_id'],
                    service_id=row['service_id'],
                    trip_id=row['trip_id'],
                    trip_headsign=row['trip_headsign'],
                    trip_short_name=row['trip_short_name'],
                    direction_id=direction_id,
                    block_id=row['block_id'],
                    shape_id=row['shape_id'],
                    jp_trip_desc=row['jp_trip_desc'],
                    registrant=registrant,
                    route_obj=route_obj,
                    service_obj=service_obj,
#                    jp_office_obj=jp_office_obj
                )

                for shape in Shapes.objects.filter(shape_id=row['shape_id'], registrant=registrant):
                    trips.shapes.add(shape)

        # Stops テーブルのインポート
        with open('/backend/api/gtfs_data/stops.txt', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                location_type_str = row.get('location_type', '')
                if location_type_str and location_type_str.strip().replace('.', '').isdigit():
                    location_type = int(float(location_type_str))
                else:
                    location_type = None

                Stops.objects.create(
                    stop_id=row['stop_id'],
                    stop_code=row['stop_code'],
                    stop_name=row['stop_name'],
                    stop_desc=row['stop_desc'],
                    stop_lat=row['stop_lat'],
                    stop_lon=row['stop_lon'],
                    zone_id=row['zone_id'],
                    stop_url=row['stop_url'],
                    location_type=location_type,
                    platform_code=row['platform_code'],
                    registrant=registrant
                )

        # StopTimes テーブルのインポート
        with open('/backend/api/gtfs_data/stop_times.txt', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                trip_obj = Trips.objects.get(trip_id=row['trip_id'], registrant=registrant)
                stop_obj = Stops.objects.get(stop_id=row['stop_id'], registrant=registrant)
                pickup_type_str = row.get('pickup_type', '')
                if pickup_type_str and pickup_type_str.strip().replace('.', '').isdigit():
                    pickup_type = int(float(pickup_type_str))
                else:
                    pickup_type = None
                drop_off_type_str = row.get('drop_off_type', '')
                if drop_off_type_str and drop_off_type_str.strip().replace('.', '').isdigit():
                    drop_off_type = int(float(drop_off_type_str))
                else:
                    drop_off_type = None
                timepoint_str = row.get('timepoint', '')
                if timepoint_str and timepoint_str.strip().replace('.', '').isdigit():
                    timepoint = int(float(timepoint_str))
                else:
                    timepoint = None
                Stop_Times.objects.create(
                    trip_id=row['trip_id'],
                    arrival_time=row['arrival_time'],
                    departure_time=row['departure_time'],
                    stop_id=row['stop_id'],
                    stop_sequence=row['stop_sequence'],
                    stop_headsign=row['stop_headsign'],
                    pickup_type=pickup_type,
                    drop_off_type=drop_off_type,
                    timepoint=timepoint,
                    registrant=registrant,
                    trip_obj=trip_obj,
                    stop_obj=stop_obj
                )
    
        # FareRules テーブルのインポート
        with open('/backend/api/gtfs_data/fare_rules.txt', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    fare_obj = Fare_Attributes.objects.get(fare_id=row['fare_id'], registrant=registrant)
                except Fare_Attributes.DoesNotExist:
                    fare_obj = no_fair_attributes
                route_obj = Routes.objects.filter(route_id=row['route_id'], registrant=registrant).first()
                origin_obj = Stops.objects.filter(stop_id=row['origin_id'], registrant=registrant).first()
                destination_obj = Stops.objects.filter(stop_id=row['destination_id'], registrant=registrant).first()
                try:
                    Fare_Rules.objects.create(
                        fare_id=row['fare_id'],
                        route_id=row['route_id'],
                        origin_id=row['origin_id'],
                        destination_id=row['destination_id'],
                        registrant=registrant,
                        fare_obj=fare_obj,
                        route_obj=route_obj,
                        origin_obj=origin_obj,
                        destination_obj=destination_obj
                    )
                except IntegrityError:
                    continue
        
        # transfer テーブルのインポート
        with open('/backend/api/gtfs_data/transfers.txt', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                from_stop_obj = Stops.objects.get(stop_id=row['from_stop_id'], registrant=registrant)
                to_stop_obj = Stops.objects.get(stop_id=row['to_stop_id'], registrant=registrant)
                Transfers.objects.create(
                    from_stop_id=row['from_stop_id'],
                    to_stop_id=row['to_stop_id'],
                    transfer_type=row['transfer_type'],
                    min_transfer_time=row['min_transfer_time'],
                    registrant=registrant,
                    from_stop_obj=from_stop_obj,
                    to_stop_obj=to_stop_obj
                )
