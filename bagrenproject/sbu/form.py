from django import forms

from .models import Sbu


class SbuForm(forms.ModelForm):
    class Meta:
        model = Sbu
        fields = (
            'provinsi',
            'uang_harian',
        )
