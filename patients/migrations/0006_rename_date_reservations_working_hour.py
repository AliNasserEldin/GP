# Generated by Django 5.0.2 on 2024-03-08 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0005_reservations'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservations',
            old_name='date',
            new_name='working_hour',
        ),
    ]
