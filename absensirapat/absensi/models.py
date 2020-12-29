from django.db import models


# Create your models here.
# https://pynative.com/python-generate-random-string/

class Rapat(models.Model):
    kode = models.CharField(max_length=5)
    tanggal = models.DateTimeField()
    meeting_id = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    pimpinan_rapat = models.CharField(max_length=50)
    agenda = models.TextField()
