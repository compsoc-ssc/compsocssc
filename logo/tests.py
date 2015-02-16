import os
from django.test import TestCase
from django.core.files import File
from logo import models
from django.conf import settings

class LogoTestCase(TestCase):
    def setUp(self):
        f=open(os.path.join(settings.BASE_DIR,'staticfiles','logo.png'),'rb')
        sub=models.Submission()
        sub.name='a'*50
        sub.college_name='b'*50
        sub.email='a@g.com'
        sub.logo=File(f)
        sub.tagline='t'*99
        sub.save()
        self.s=sub
    def test_str_function(self):
        self.assertEqual(self.s.__str__(),'a'*50)
