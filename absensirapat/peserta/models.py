from django.db import models

# Create your models here.
from absensi.models import Rapat


class Peserta(models.Model):
    rapat_id = models.ForeignKey(Rapat, on_delete=models.CASCADE, related_name='peserta_agenda')
    nip = models.CharField(max_length=20)
    nama = models.CharField(max_length=50)
    jabatan = models.CharField(max_length=50)
    unit_kerja = models.CharField(max_length=255)
