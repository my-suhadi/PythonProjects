from django.db import models


# Create your models here.

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
    nama = models.CharField(max_length=20)
    golongan = models.ForeignKey(Golongan, on_delete=models.DO_NOTHING)
    jabatan = models.ForeignKey(Jabatan, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nama
