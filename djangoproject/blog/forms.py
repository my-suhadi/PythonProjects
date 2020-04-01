from django import forms

# model dr models.py
from .models import Artikel

class ArtikelForm(forms.ModelForm):
    class Meta:
        model = Artikel
        fields = [
            'judul',
            'isi',
            'penulis',
        ]