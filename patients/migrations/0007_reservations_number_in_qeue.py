# Generated by Django 5.0.2 on 2024-03-08 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0006_rename_date_reservations_working_hour'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservations',
            name='number_in_qeue',
            field=models.IntegerField(default=1),
        ),
    ]
