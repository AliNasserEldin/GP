# Generated by Django 5.0.2 on 2024-03-01 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0002_remove_user_phone_user_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]
