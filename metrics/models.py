from django.db import models
from django.utils import timezone
import requests

class Hit(models.Model):
    ip = models.GenericIPAddressField()
    ua = models.CharField(max_length=200)
    url = models.CharField(max_length=500, default='/')
    stamp = models.DateTimeField(auto_now_add=True)
