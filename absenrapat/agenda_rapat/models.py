from django.db import models

# Create your models here.

class AgendaRapat(models.Model):
    judul = models.CharField(max_length=255)
    tanggal = models.DateTimeField
