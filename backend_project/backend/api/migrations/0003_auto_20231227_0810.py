# Generated by Django 3.2.23 on 2023-12-26 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20231227_0808'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trips',
            name='jp_office_id',
        ),
        migrations.RemoveField(
            model_name='trips',
            name='jp_trip_desc_symbol',
        ),
    ]
