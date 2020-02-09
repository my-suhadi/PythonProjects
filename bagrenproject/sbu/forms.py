from django import forms

from .models import sbu

class sbuForm(forms.ModelForm):
    class Meta:
        model = sbu
        fields = (
        	'provinsi',
        	'uang_harian',
        	)