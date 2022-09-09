from django.db import models


class AllergyProfile(models.Model):

    # Allergy options
    FOOD = 'FOOD'
    MED = 'MED'
    ENV = 'ENV'
    OTH = 'OTH'

    ALLERGY_CHOICES = [
        (FOOD, 'Food'),
        (MED, 'Medication'),
        (ENV, 'Environmental'),
        (OTH, 'Other'),
    ]

    allergy_type = models.Model()
    allergy_name = models.Model()
    allergy_reaction = models.Model()
    allergy_intervention = models.Model()
    allergy_notes = models.Model()


class UserProfile(models.Model):

    # Blood type options
    O_POS = 'O+'
    O_NEG = 'O-'
    A_POS = 'A+'
    A_NEG = 'A-'
    B_POS = 'B+'
    B_NEG = 'B-'
    AB_POS = 'AB+'
    AB_NEG = 'AB-'
    UNK = 'UNK'

    # User options
    SELF = 'SF'
    SPOUSE = 'SO'
    CHILD = 'CH'
    PARENT = 'PRT'
    GRAND = 'GRP'
    EXTEND = 'EXT'

    # Prefix options
    DR = 'DR'
    MR = 'MR'
    MS = 'MS'
    MRS = 'MRS'
    NONE = 'NONE'

    BLOOD_TYPES_CHOICES = [
        (O_POS, 'O Positive'),
        (O_NEG, 'O Negative'),
        (A_POS, 'A Positive'),
        (A_NEG, 'A Negative'),
        (B_POS, 'B Positive'),
        (B_NEG, 'B Negative'),
        (AB_POS, 'AB Positive'),
        (AB_NEG, 'AB Negative'),
        (UNK, 'Unknown'),
    ]

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

    prefix = models.CharField('Prefix', max_length=4,
                              blank=True, choices=PREFIX_CHOICES, default=NONE)
    first_name = models.CharField('First Name', max_length=50, blank=False)
    last_name = models.CharField('Last Name', max_length=50, blank=False)
    date_of_birth = models.DateField('Date of Birth', blank=False)
    height_ft = models.IntegerField('Height(ft)', blank=False)
    height_in = models.IntegerField('Height(in)', blank=True, null=True)
    weight_lbs = models.IntegerField('Weight(lbs)', blank=False)
    blood_type = models.CharField(
        'Blood Type', max_length=10, blank=False, choices=BLOOD_TYPES_CHOICES)
    address = models.CharField(
        'Address', max_length=150, blank=True, null=True)
    email = models.EmailField('Email', max_length=150, blank=True, null=True)
    phone = models.CharField(
        'Contact Phone', max_length=20, blank=True, null=True)
    pcp = models.CharField('Primary Care Provider',
                           max_length=120, blank=True, null=True)
    pcp_address = models.CharField(
        'Provider Address', max_length=120, blank=True, null=True)
    pcp_number = models.IntegerField(
        'Provider Number', blank=True, null=True)
    emergency_contact = models.CharField(
        'Emergency Contact', max_length=50, blank=True, null=True)
    emergency_phone = models.CharField(
        'Emergency Phone Number', max_length=20, blank=True, null=True)
    relationship = models.CharField(
        'Relationship', max_length=3, choices=RELATIONSHIP_CHOICES, default=SELF)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
