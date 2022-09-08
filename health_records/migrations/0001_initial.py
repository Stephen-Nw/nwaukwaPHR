# Generated by Django 4.0.5 on 2022-09-08 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prefix', models.CharField(blank=True, choices=[('DR', 'Dr.'), ('MR', 'Mr.'), ('MS', 'Ms.'), ('MRS', 'Mrs.'), ('NONE', ' ')], default='NONE', max_length=4, verbose_name='Prefix')),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last Name')),
                ('date_of_birth', models.DateField(verbose_name='Date of Birth')),
                ('height_ft', models.IntegerField(verbose_name='Height(ft)')),
                ('height_in', models.IntegerField(blank=True, verbose_name='Height(in)')),
                ('weight_lbs', models.IntegerField(verbose_name='Weight(lbs)')),
                ('blood_type', models.CharField(max_length=10, verbose_name='Blood Type')),
                ('address', models.CharField(blank=True, max_length=150, verbose_name='Address')),
                ('email', models.EmailField(blank=True, max_length=150, verbose_name='Email')),
                ('phone', models.CharField(blank=True, max_length=20, verbose_name='Contact Phone')),
                ('pcp', models.CharField(blank=True, max_length=120, verbose_name='Primary Care Provider')),
                ('pcp_address', models.CharField(blank=True, max_length=120, verbose_name='Provider Address')),
                ('pcp_number', models.IntegerField(blank=True, verbose_name='Provider Number')),
                ('emergency_contact', models.CharField(blank=True, max_length=50, verbose_name='Emergency Contact')),
                ('emergency_phone', models.CharField(blank=True, max_length=20, verbose_name='Emergency Phone Number')),
                ('relationship', models.CharField(choices=[('SF', 'Self'), ('SO', 'Spouse'), ('CH', 'Child'), ('PRT', 'Parent'), ('GRP', 'Grandparent'), ('EXT', 'Extended Family')], default='SF', max_length=3, verbose_name='Relationship')),
            ],
        ),
    ]
