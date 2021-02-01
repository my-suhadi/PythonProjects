from django import forms

from .models import Peserta


class PesertaForm(forms.ModelForm):

    class Meta:
        model = Peserta
        fields = '__all__'
        exclude = ('rapat_id',)
        labels = {
            'nip': 'NIP',
            'unit_kerja': 'Unit Kerja',
            'no_hp': 'No. HP',
        }
