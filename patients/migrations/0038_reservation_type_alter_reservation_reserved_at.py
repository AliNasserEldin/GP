# Generated by Django 5.0.3 on 2024-05-05 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0037_alter_reservation_reserved_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='type',
            field=models.CharField(choices=[('S', 'Surgery'), ('C', 'Consultation'), ('V', 'Visit'), ('E', 'Examination')], default='C', max_length=1),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='reserved_at',
            field=models.CharField(default='2024-05-05 17:33:20', max_length=30),
        ),
    ]
