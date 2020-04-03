from django.db import models

# Create your models here.
from django.utils.text import slugify


class Artikel(models.Model):
    judul = models.CharField(max_length=255)
    isi = models.TextField()
    kategori = models.CharField(max_length=255)
    published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(blank=True, editable=False)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.judul)
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return "{}. {}".format(self.id, self.judul)