import os
from django.test import TestCase
from django.core.files import File
from events.logo import models
from django.conf import settings


class LogoTestCase(TestCase):
    def setup(self):
        f = open(os.path.join(settings.BASE_DIR, 'static','images/logo.png'), 'rb')
        sub = models.Submission()
        sub.name = 'Jon Smith'
        sub.college_name = 'SSC'
        sub.email='jon@smith.com'
        sub.logo = File(f)
        sub.tagline = 'Hello World!'
        sub.save()
        self.s = sub

    def test_str_function(self):
        self.assertEqual(self.s.__str__(), 'Jon Smith')
