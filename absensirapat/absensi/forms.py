from django import forms

from absensi.models import Rapat


class RapatForm(forms.ModelForm):
    class Meta:
        model = Rapat
        fields = '__all__'
        exclude = ('tanggal',)
