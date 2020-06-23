from django.db import models


# Create your models here.

class profile(models.Model):
    name = models.CharField(max_length=120)
    desc = models.TextField()

    def __unicode__(self):
        return self.name
