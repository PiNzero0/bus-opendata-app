# Generated by Django 3.2.23 on 2023-12-27 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20231227_1717'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fare_rules',
            name='contains_id',
        ),
    ]
