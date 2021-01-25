from django.db import models

# Create your models here.
from absensi.models import Rapat


class Peserta(models.Model):
    rapat_id = models.ForeignKey(Rapat, on_delete=models.CASCADE, related_name='peserta_agenda')
    nip = models.CharField(max_length=20)
    nama = models.CharField(max_length=50)
    jabatan = models.CharField(max_length=50)
    unit_kerja = models.CharField(max_length=255)


class Bagian (models.Model):
    nama = models.CharField(max_length=50)

    def __str__(self):
        return self.nama


class Golongan(models.Model):
    gol = models.CharField(max_length=5)
    pangkat = models.CharField(max_length=30)

    def __str__(self):
        return self.gol


class Jabatan(models.Model):
    nama = models.CharField(max_length=50)

    def __str__(self):
        return self.nama


class Pegawai(models.Model):
    nip = models.CharField(max_length=20)
    nama = models.CharField(max_length=50)
    golongan = models.ForeignKey(Golongan, models.DO_NOTHING, 'golongan_pegawai')
    jabatan = models.ForeignKey(Jabatan, models.DO_NOTHING, 'jabatan_pegawai')
    bagian = models.ForeignKey(Bagian, models.DO_NOTHING, 'bagian_pegawai')

    def __str__(self):
        return self.nama
