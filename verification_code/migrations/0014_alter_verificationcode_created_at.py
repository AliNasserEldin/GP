# Generated by Django 5.0.3 on 2024-04-20 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verification_code', '0013_alter_verificationcode_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verificationcode',
            name='created_at',
            field=models.CharField(default=' 2024-04-20 18:32:23', max_length=30),
        ),
    ]
