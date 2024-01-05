
docker-compose up -d

docker-compose exec backend bash

python manage.py makemigrations
python manage.py migrate
python manage.py import_gtfs
