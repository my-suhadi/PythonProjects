from django.db import models

# Create your models here.


class Rapat(models.Model):
    tanggal = models.DateTimeField(auto_now_add=True)
    meeting_id = models.CharField(max_length=15)
    password = models.CharField(max_length=15)
    pimpinan_rapat = models.CharField(max_length=50)
    agenda = models.TextField()


class Peserta(models.Model):
    rapat_id = models.ForeignKey(Rapat, on_delete=models.CASCADE, related_name='peserta_agenda')
    nama = models.CharField(max_length=50)
    nip = models.CharField(max_length=20)
    jabatan = models.CharField(max_length=50)
    unit_kerja = models.CharField(max_length=255)

