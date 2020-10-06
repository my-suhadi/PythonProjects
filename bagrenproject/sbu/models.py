from django.db import models

# Create your models here.
from bagren.common import generate_uuid


class Sbu(models.Model):
    sbu_id = models.CharField(max_length=40, primary_key=True, editable=False)
    provinsi = models.CharField(max_length=100)
    uang_harian = models.FloatField()

    # override methods
    def __str__(self):
        return "{}. {}".format(self.id, self.provinsi)

    def save(self, **kwargs):
        self.sbu_id = generate_uuid()
        super(Sbu, self).save()
