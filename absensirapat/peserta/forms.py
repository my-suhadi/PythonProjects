from django import forms

from .models import Peserta


class PesertaForm(forms.ModelForm):
    class Meta:
        model = Peserta
        fields = '__all__'
        # exclude = ('tanggal',)
