# Generated by Django 5.0.3 on 2024-06-23 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nurses', '0004_alter_calls_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calls',
            name='date',
            field=models.CharField(default='2024-06-23 21:40:21', max_length=30),
        ),
    ]
