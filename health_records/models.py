from django.db import models


# Model based on user's immunization hx
class ImmunizationProfile(models.Model):
    # Reaction options
    Y = 'Y'
    N = 'N'

    REACTION_CHOICES = [
        (Y, 'Yes'),
        (N, 'No'),
    ]

    vaccine_name = models.CharField(
        'Vaccine Name', max_length=100, blank=False)
    vaccine_date = models.DateField('Date Last Received', blank=False)
    vaccine_reaction = models.CharField(
        'Adverse Reactions', blank=False, max_length=3, choices=REACTION_CHOICES)
    vaccine_rxn_if_positive = models.TextField(
        'Describe reaction (Leave blank if none)', blank=True, null=True)
    vaccine_next_due = models.DateField('Next Due Date', blank=True)
    vaccine_notes = models.TextField('Additional Notes', blank=True, null=True)

    def __str__(self):
        return self.vaccine_name


# Model based on user's med/surg hx
class MedicalHistoryProfile(models.Model):
    # History options
    SURG = 'SURG'
    MED = 'MED'

    HISTORY_CHOICES = [
        (SURG, 'Surgical'),
        (MED, 'Medical'),
    ]

    hx_type = models.CharField(
        'Type', max_length=5, blank=False, choices=HISTORY_CHOICES)
    hx_date = models.DateField('Date', blank=False)
    hx_diagnosis = models.CharField('Diagnosis', max_length=100, blank=False)
    hx_procedure = models.CharField(
        'Procedure', max_length=100, blank=True, null=True)
    hx_medications = models.CharField(
        'Medications', max_length=300, blank=True, null=True)
    hx_notes = models.TextField('Additional Notes', blank=True, null=True)

    def __str__(self):
        return self.hx_date


# Model based on user's appointments
class AppointmentProfile(models.Model):
    appt_date = models.DateField('Date', blank=False)
    appt_time = models.TimeField('Time', blank=False)
    appt_provider = models.CharField('Provider', max_length=50, blank=False)
    appt_address = models.CharField(
        'Address', max_length=300, blank=True, null=True)
    appt_instructions = models.TextField(
        'Additional Instructions', blank=True, null=True)

    def __str__(self):
        return self.appt_date


# Model based on user's med list
class MedicationProfile(models.Model):
    med_name = models.CharField('Medication Name', max_length=50, blank=False)
    med_indication = models.CharField(
        'Clinical Indication', max_length=150, blank=False)
    med_dosage = models.CharField('Dosage', max_length=50, blank=False)
    med_frequency = models.CharField('Frequency', max_length=50, blank=False)
    med_start = models.CharField(
        'Start Date', max_length=50, blank=True, null=True)
    med_duration = models.CharField(
        'Duration', max_length=50, blank=True, null=True)
    med_ongoing = models.BooleanField('Currently Taking', default=False)

    def __str__(self):
        return self.med_name


# Model based on user's allergies
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

    allergy_type = models.CharField(
        'Allergy Type', max_length=5, blank=False, choices=ALLERGY_CHOICES)
    allergy_name = models.CharField(
        'Allergic Substance', max_length=50, blank=False)
    allergy_reaction = models.CharField(
        'Allergic Reaction', max_length=150, blank=False)
    allergy_intervention = models.TextField(
        'Intervention/Treatment', blank=True, null=True)
    allergy_notes = models.TextField('Additional Notes', blank=True, null=True)


# Model to set up user's profile
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
