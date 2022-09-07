from django.db import models


class UserProfile(models.Model):

    SELF = 'SF'
    SPOUSE = 'SO'
    CHILD = 'CH'
    PARENT = 'PRT'
    GRAND = 'GRP'
    EXTEND = 'EXT'

    DR = 'DR'
    MR = 'MR'
    MS = 'MS'
    MRS = 'MRS'
    NONE = 'NONE'

    RELATIONSHIP_CHOICES = [
        (SELF, 'Self'),
        (SPOUSE, 'Spouse'),
        (CHILD, 'Child'),
        (PARENT, 'Parent'),
        (GRAND, 'Grandparent'),
        (EXTEND, 'Extended Family'),
    ]

    PREFIX_CHOICES = [
        (DR, 'Dr.'),
        (MR, 'Mr.'),
        (MS, 'Ms.'),
        (MRS, 'Mrs.'),
        (NONE, ' '),

    ]

    prefix = models.CharField('Prefix', max_length=2,
                              blank=True, choices=PREFIX_CHOICES, default=NONE)
    first_name = models.CharField('First Name', max_length=50, blank=False)
    last_name = models.CharField('Last Name', max_length=50, blank=False)
    date_of_birth = models.DateField('Date of Birth')
    height_ft = models.IntegerField('Height(ft)', max_length=2)
    height_in = models.IntegerField('Height(in)', max_length=2)
    weight_lbs = models.IntegerField('Weight(lbs)', max_length=3)
    blood_type = models.CharField('Blood Type', max_length=10)
    address = models.CharField('Address', max_length=150)
    email = models.CharField('Email', max_length=150)
    phone = models.CharField('Contact Phone', max_length=20)
    pcp = models.CharField('Primary Care Provider', max_length=120)
    pcp_address = models.CharField('Provider Address', max_length=120)
    pcp_number = models.IntegerField('Provider Number', max_length=20)
    emergency_contact = models.CharField('Emergency Contact', max_length=50)
    emergency_phone = models.CharField('Emergency Phone Number', max_length=20)
    relationship = models.CharField(
        'Relationship', max_length=2, choices=RELATIONSHIP_CHOICES, default=SELF)
