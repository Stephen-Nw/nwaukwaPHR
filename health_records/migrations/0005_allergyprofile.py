# Generated by Django 4.0.5 on 2022-09-13 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_records', '0004_alter_userprofile_blood_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllergyProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allergy_type', models.CharField(choices=[('FOOD', 'Food'), ('MED', 'Medication'), ('ENV', 'Environmental'), ('OTH', 'Other')], max_length=5, verbose_name='Allergy Type')),
                ('allergy_name', models.CharField(max_length=50, verbose_name='Allergic Substance')),
                ('allergy_reaction', models.CharField(max_length=150, verbose_name='Allergic Reaction')),
                ('allergy_intervention', models.TextField(blank=True, verbose_name='Intervention/Treatment')),
                ('allergy_notes', models.TextField(blank=True, verbose_name='Additional Notes')),
            ],
        ),
    ]
