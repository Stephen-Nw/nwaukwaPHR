# Generated by Django 4.0.5 on 2022-09-22 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_records', '0009_alter_appointmentprofile_appt_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalHistoryProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hx_type', models.CharField(choices=[('SURG', 'Surgical'), ('MED', 'Medical')], max_length=5, verbose_name='Type')),
                ('hx_date', models.DateField(verbose_name='Date')),
                ('hx_diagnosis', models.CharField(max_length=100, verbose_name='Diagnosis')),
                ('hx_procedure', models.CharField(blank=True, max_length=100, null=True, verbose_name='Procedure')),
                ('hx_medications', models.CharField(blank=True, max_length=300, null=True, verbose_name='Medications')),
                ('hx_notes', models.TextField(blank=True, null=True, verbose_name='Additional Notes')),
            ],
        ),
    ]
