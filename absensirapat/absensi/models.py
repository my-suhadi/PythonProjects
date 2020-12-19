from django.db import models


# Create your models here.


class Rapat(models.Model):
    tanggal = models.DateTimeField(auto_now_add=True)
    meeting_id = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    pimpinan_rapat = models.CharField(max_length=50)
    agenda = models.TextField()
