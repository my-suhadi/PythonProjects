from django.db import models

# Create your models here.
from bagren.common import generate_uuid


class Pangkat(models.Model):
    pangkat_id = models.CharField(max_length=40, primary_key=True)
    nomer_urut = models.PositiveSmallIntegerField()
    pangkat_name = models.CharField(max_length=30)
    golongan = models.CharField(max_length=5)

    # override methods
    def __str__(self):
        return "{}. {}".format(self.nomer_urut, self.pangkat_name)

    def save(self, **kwargs):
        self.pangkat_id = generate_uuid()
        super(Pangkat, self).save()


class Pegawai(models.Model):
    pegawai_id = models.CharField(max_length=40, primary_key=True)
    nama = models.CharField(max_length=50)
    pangkat = models.CharField(max_length=40)
    nip = models.IntegerField()

    # override methods
    # def __str__(self):
    #     return "{}. {}".format(self.nomer_urut, self.pangkat_name)

    def save(self, **kwargs):
        self.pegawai_id = generate_uuid()
        super(Pegawai, self).save()
