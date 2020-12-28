from django import forms

from .models import Rapat


class RapatForm(forms.ModelForm):
    class Meta:
        model = Rapat
        fields = '__all__'
        exclude = ('tanggal',)
