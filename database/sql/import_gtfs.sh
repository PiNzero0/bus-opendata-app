#!/bin/bash

# テーブル作成のSQLファイルを実行
psql -U user -d db -f /docker-entrypoint-initdb.d/create-tables.sql

# PostgreSQL 接続情報
PG_USER="user"
PG_DB="db"

# GTFS データが格納されているディレクトリ
GTFS_DATA_DIR="./gtfs-data"

# agency テーブル
psql -U $PG_USER -d $PG_DB -c "\COPY public.agency FROM '$GTFS_DATA_DIR/agency.txt' WITH CSV HEADER DELIMITER ','"

# agency_jp テーブル
psql -U $PG_USER -d $PG_DB -c "\COPY public.agency_jp FROM '$GTFS_DATA_DIR/agency_jp.txt' WITH CSV HEADER DELIMITER ','"

# stops テーブル
psql -U $PG_USER -d $PG_DB -c "\COPY public.stops FROM '$GTFS_DATA_DIR/stops.txt' WITH CSV HEADER DELIMITER ','"

# routes テーブル
psql -U $PG_USER -d $PG_DB -c "\COPY public.routes FROM '$GTFS_DATA_DIR/routes.txt' WITH CSV HEADER DELIMITER ','"

# routes_jp テーブル
psql -U $PG_USER -d $PG_DB -c "\COPY public.routes_jp FROM '$GTFS_DATA_DIR/routes_jp.txt' WITH CSV HEADER DELIMITER ','"

# trips テーブル
psql -U $PG_USER -d $PG_DB -c "\COPY public.trips FROM '$GTFS_DATA_DIR/trips.txt' WITH CSV HEADER DELIMITER ','"

# office_jp テーブル
psql -U $PG_USER -d $PG_DB -c "\COPY public.office_jp FROM '$GTFS_DATA_DIR/office_jp.txt' WITH CSV HEADER DELIMITER ','"

# stop_times テーブル
psql -U $PG_USER -d $PG_DB -c "\COPY public.stop_times FROM '$GTFS_DATA_DIR/stop_times.txt' WITH CSV HEADER DELIMITER ','"

# calendar テーブル
psql -U $PG_USER -d $PG_DB -c "\COPY public.calendar FROM '$GTFS_DATA_DIR/calendar.txt' WITH CSV HEADER DELIMITER ','"

# calendar_dates テーブル
psql -U $PG_USER -d $PG_DB -c "\COPY public.calendar_dates FROM '$GTFS_DATA_DIR/calendar_dates.txt' WITH CSV HEADER DELIMITER ','"

# fare_attributes テーブル
psql -U $PG_USER -d $PG_DB -c "\COPY public.fare_attributes FROM '$GTFS_DATA_DIR/fare_attributes.txt' WITH CSV HEADER DELIMITER ','"

# fare_rules テーブル
psql -U $PG_USER -d $PG_DB -c "\COPY public.fare_rules FROM '$GTFS_DATA_DIR/fare_rules.txt' WITH CSV HEADER DELIMITER ','"

# shapes テーブル
psql -U $PG_USER -d $PG_DB -c "\COPY public.shapes FROM '$GTFS_DATA_DIR/shapes.txt' WITH CSV HEADER DELIMITER ','"

# frequencies テーブル
psql -U $PG_USER -d $PG_DB -c "\COPY public.frequencies FROM '$GTFS_DATA_DIR/frequencies.txt' WITH CSV HEADER DELIMITER ','"

# transfers テーブル
psql -U $PG_USER -d $PG_DB -c "\COPY public.transfers FROM '$GTFS_DATA_DIR/transfers.txt' WITH CSV HEADER DELIMITER ','"

# feed_info テーブル
psql -U $PG_USER -d $PG_DB -c "\COPY public.feed_info FROM '$GTFS_DATA_DIR/feed_info.txt' WITH CSV HEADER DELIMITER ','"

# translations テーブル
psql -U $PG_USER -d $PG_DB -c "\COPY public.translations FROM '$GTFS_DATA_DIR/translations.txt' WITH CSV HEADER DELIMITER ','"
