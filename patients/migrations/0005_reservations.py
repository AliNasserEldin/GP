# Generated by Django 5.0.2 on 2024-03-07 21:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0003_remove_clinic_doctor_id_remove_workinghour_doctor_id_and_more'),
        ('patients', '0004_user_clinic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clinic', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='doctors.clinic')),
                ('date', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='doctors.workinghour')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
