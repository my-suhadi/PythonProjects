from django.db import models


# Create your models here.

class Bagian(models.Model):
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

    def __str__(self):
        return self.nama
