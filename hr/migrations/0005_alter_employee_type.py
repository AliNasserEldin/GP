# Generated by Django 5.0.3 on 2024-06-23 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0004_employee_clinic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='type',
            field=models.CharField(choices=[('A', 'Admin'), ('D', 'Doctor'), ('N', 'Nurse'), ('H', 'Human Resources'), ('P', 'Pharmacist'), ('HD', 'Head Doctor'), ('HN', 'Head Nurse')], default='P', max_length=2),
        ),
    ]
