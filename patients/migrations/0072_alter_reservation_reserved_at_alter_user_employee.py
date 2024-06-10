# Generated by Django 5.0.3 on 2024-06-10 22:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0004_employee_clinic'),
        ('patients', '0071_alter_reservation_reserved_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='reserved_at',
            field=models.CharField(default='2024-06-10 22:23:56', max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='employee',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hr.employee'),
        ),
    ]
