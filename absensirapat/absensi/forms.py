from django import forms

from .models import Rapat


class RapatForm(forms.ModelForm):
    tanggal = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])

    class Meta:
        model = Rapat
        fields = '__all__'
        exclude = ('kode',)
        labels = {
            'meeting_id': 'Meeting ID',
        }


class LoginForm(forms.Form):
    uname = forms.CharField(max_length=18, label='Username')
    passwd = forms.CharField(widget=forms.PasswordInput, label='Password')

