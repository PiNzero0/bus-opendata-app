#init-database.sh
#!/usr/bin/env bash
docker-compose exec database bash -c "./docker-entrypoint-initdb.d/import_gtfs.sh"

psql -U user -d db < "/docker-entrypoint-initdb.d/create-tables.sql"