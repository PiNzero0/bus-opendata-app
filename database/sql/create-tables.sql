-- 拡張をインストール
CREATE EXTENSION IF NOT EXISTS postgis;

-- スキーマ作成
CREATE SCHEMA IF NOT EXISTS public;

-- テーブル削除
DROP TABLE IF EXISTS gtfs;

--gtfsファイルの中身をすべて格納するテーブル
--agency テーブル
CREATE TABLE IF NOT EXISTS public.agency (
    agency_id VARCHAR(255),
    agency_name VARCHAR(255),
    agency_url VARCHAR(255),
    agency_timezone VARCHAR(255),
    agency_lang VARCHAR(255),
    agency_phone VARCHAR(255),
    agency_fare_url VARCHAR(255),
    agency_email VARCHAR(255)
);

--agency_jp テーブル
CREATE TABLE IF NOT EXISTS public.agency_jp (
    agency_jp VARCHAR(255),
    agency_id VARCHAR(255),
    agency_name VARCHAR(255),
    agency_url VARCHAR(255),
    agency_timezone VARCHAR(255),
    agency_lang VARCHAR(255),
    agency_phone VARCHAR(255),
    agency_fare_url VARCHAR(255),
    agency_email VARCHAR(255)
);
-- stops テーブル
CREATE TABLE IF NOT EXISTS public.stops (
    stop_id VARCHAR(255),
    stop_code VARCHAR(255),
    stop_name VARCHAR(255),
    stop_desc VARCHAR(255),
    stop_lat DOUBLE PRECISION,
    stop_lon DOUBLE PRECISION,
    zone_id VARCHAR(255),
    stop_url VARCHAR(255),
    location_type INTEGER,
    parent_station VARCHAR(255),
    wheelchair_boarding INTEGER,
    platform_code VARCHAR(255)
);

-- routes テーブル
CREATE TABLE IF NOT EXISTS public.routes (
    route_id VARCHAR(255),
    agency_id VARCHAR(255),
    route_short_name VARCHAR(255),
    route_long_name VARCHAR(255),
    route_desc VARCHAR(255),
    route_type INTEGER,
    route_color VARCHAR(255),
    route_text_color VARCHAR(255)
);

-- routes_jp テーブル
CREATE TABLE IF NOT EXISTS public.routes_jp (
    route_jp VARCHAR(255),
    route_id VARCHAR(255),
    route_update_date VARCHAR(255),
    origin_stop VARCHAR(255),
    via_stop VARCHAR(255),
    destination_stop VARCHAR(255)
);

-- trips テーブル
CREATE TABLE IF NOT EXISTS public.trips (
    route_id VARCHAR(255),
    service_id VARCHAR(255),
    trip_id VARCHAR(255),
    trip_headsign VARCHAR(255),
    direction_id INTEGER,
    block_id VARCHAR(255),
    shape_id VARCHAR(255),
    wheelchair_accessible INTEGER,
    bikes_allowed INTEGER,
    jp_trip_desc VARCHAR(255),
    jp_trip_desc_symbol VARCHAR(255),
    jp_office_id VARCHAR(255)
);

-- office_jp テーブル
CREATE TABLE IF NOT EXISTS public.office_jp (
    office_id VARCHAR(255),
    office_name VARCHAR(255),
    office_url VARCHAR(255),
    office_phone VARCHAR(255)
);
-- stop_times テーブル
CREATE TABLE IF NOT EXISTS public.stop_times (
    trip_id VARCHAR(255),
    arrival_time VARCHAR(255),
    departure_time VARCHAR(255),
    stop_id VARCHAR(255),
    stop_sequence INTEGER,
    stop_headsign VARCHAR(255),
    pickup_type INTEGER,
    drop_off_type INTEGER,
    shape_dist_traveled DOUBLE PRECISION
);

-- calendar テーブル
CREATE TABLE IF NOT EXISTS public.calendar (
    service_id VARCHAR(255),
    monday INTEGER,
    tuesday INTEGER,
    wednesday INTEGER,
    thursday INTEGER,
    friday INTEGER,
    saturday INTEGER,
    sunday INTEGER,
    start_date VARCHAR(255),
    end_date VARCHAR(255)
);

-- calendar_dates テーブル
CREATE TABLE IF NOT EXISTS public.calendar_dates (
    service_id VARCHAR(255),
    date VARCHAR(255),
    exception_type INTEGER
);

-- fare_attributes テーブル
CREATE TABLE IF NOT EXISTS public.fare_attributes (
    fare_id VARCHAR(255),
    price DOUBLE PRECISION,
    currency_type VARCHAR(255),
    payment_method INTEGER,
    transfers INTEGER,
    transfer_duration VARCHAR(255)
);

-- fare_rules テーブル
CREATE TABLE IF NOT EXISTS public.fare_rules (
    fare_id VARCHAR(255),
    route_id VARCHAR(255),
    origin_id VARCHAR(255),
    destination_id VARCHAR(255),
    contains_id VARCHAR(255)
);

-- shapes テーブル
CREATE TABLE IF NOT EXISTS public.shapes (
    shape_id VARCHAR(255),
    shape_pt_lat DOUBLE PRECISION,
    shape_pt_lon DOUBLE PRECISION,
    shape_pt_sequence INTEGER,
    shape_dist_traveled DOUBLE PRECISION
);

-- frequencies テーブル
CREATE TABLE IF NOT EXISTS public.frequencies (
    trip_id VARCHAR(255),
    start_time VARCHAR(255),
    end_time VARCHAR(255),
    headway_secs INTEGER,
    exact_times INTEGER
);

-- transfers テーブル
CREATE TABLE IF NOT EXISTS public.transfers (
    from_stop_id VARCHAR(255),
    to_stop_id VARCHAR(255),
    transfer_type INTEGER,
    min_transfer_time INTEGER
);

-- feed_info テーブル
CREATE TABLE IF NOT EXISTS public.feed_info (
    feed_publisher_name VARCHAR(255),
    feed_publisher_url VARCHAR(255),
    feed_lang VARCHAR(255),
    feed_start_date VARCHAR(255),
    feed_end_date VARCHAR(255),
    feed_version VARCHAR(255)
); 

-- translations テーブル
CREATE TABLE IF NOT EXISTS public.translations (
    trans_id VARCHAR(255),
    lang VARCHAR(255),
    translation VARCHAR(255)
)