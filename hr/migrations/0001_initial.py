# Generated by Django 5.0.3 on 2024-05-14 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('D', 'Doctor'), ('A', 'Admin'), ('N', 'Nurse'), ('H', 'Human Resources')], default='P', max_length=2)),
                ('specialization', models.CharField(choices=[('AnatomicalPathology', 'AnatomicalPathology'), ('Anesthesiology', 'Anesthesiology'), ('Cardiology', 'Cardiology'), ('Cardiovascular/ThoracicSurgery', 'Cardiovascular/ThoracicSurgery'), ('ClinicalImmunology/Allergy', 'ClinicalImmunology/Allergy'), ('CriticalCareMedicine', 'CriticalCareMedicine'), ('Dermatology', 'Dermatology'), ('DiagnosticRadiology', 'DiagnosticRadiology'), ('EmergencyMedicine', 'EmergencyMedicine'), ('EndocrinologyandMetabolism', 'EndocrinologyandMetabolism'), ('FamilyMedicine', 'FamilyMedicine'), ('Gastroenterology', 'Gastroenterology'), ('GeneralInternalMedicine', 'GeneralInternalMedicine'), ('GeneralSurgery', 'GeneralSurgery'), ('General/ClinicalPathology', 'General/ClinicalPathology'), ('GeriatricMedicine', 'GeriatricMedicine'), ('Hematology', 'Hematology'), ('MedicalBiochemistry', 'MedicalBiochemistry'), ('MedicalGenetics', 'MedicalGenetics'), ('MedicalMicrobiologyandInfectiousDiseases', 'MedicalMicrobiologyandInfectiousDiseases'), ('MedicalOncology', 'MedicalOncology'), ('Nephrology', 'Nephrology'), ('Neurology', 'Neurology'), ('Neurosurgery', 'Neurosurgery'), ('NuclearMedicine', 'NuclearMedicine'), ('Obstetrics/Gynecology', 'Obstetrics/Gynecology'), ('OccupationalMedicine', 'OccupationalMedicine'), ('Ophthalmology', 'Ophthalmology'), ('OrthopedicSurgery', 'OrthopedicSurgery'), ('Otolaryngology', 'Otolaryngology'), ('Pediatrics', 'Pediatrics'), ('PhysicalMedicineandRehabilitation', 'PhysicalMedicineandRehabilitation'), ('PlasticSurgery', 'PlasticSurgery'), ('Psychiatry', 'Psychiatry'), ('PublicHealthandPreventiveMedicine', 'PublicHealthandPreventiveMedicine'), ('RadiationOncology', 'RadiationOncology'), ('Respirology', 'Respirology'), ('Rheumatology', 'Rheumatology'), ('Urology', 'Urology')], max_length=50, null=True)),
                ('salary', models.PositiveIntegerField(null=True)),
                ('hired_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
        ),
    ]