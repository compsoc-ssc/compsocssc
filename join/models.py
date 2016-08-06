from __future__ import unicode_literals

from django.core.validators import RegexValidator
from django.db import models


class NewMember(models.Model):
    courses = (
        ('ECO', 'B.A. Economics (Hons.)'),
        ('ENG', 'B.A. English (Hons.)'),
        ('HIS', 'B.A. History (Hons.)'),
        ('PHI', 'B.A. Philosophy (Hons.)'),
        ('SAN', 'B.A. Sanskrit (Hons.)'),
        ('BAP', 'B.A. Programme'),
        ('MAT', 'B.Sc. Mathematics (Hons.)'),
        ('CHM', 'B.Sc. Chemistry (Hons.)'),
        ('PHY', 'B.Sc. Physics (Hons.)'),
        ('BCM', 'B.Sc. Programme (Chemistry)'),
        ('BCS', 'B.Sc. Programme (Computer Science)'),
    )
    years = (
        (1, 'One (I)'),
        (2, 'Two (II)'),
        (3, 'Three (III)'),
    )
    name = models.CharField(max_length=50)
    phone_regex = RegexValidator(regex=r'^\d{10}$',
                                 message="Phone number must be 10 digits.")
    phone_number = models.CharField(validators=[phone_regex], blank=False, max_length=10)
    email = models.EmailField(unique=True, error_messages={'unique': "This email has already been registered."})
    course = models.CharField(max_length=50, choices=courses)
    year = models.PositiveSmallIntegerField(choices=years)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
