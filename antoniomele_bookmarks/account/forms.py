from django import forms
from django.contrib.auth.models import User

from .models import Profile


class LoginForm(forms.Form):
    uname = forms.CharField()
    passwd = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    passwd = forms.CharField(
        label='Password',
        widget=forms.PasswordInput
    )
    passwd2 = forms.CharField(
        label='Repeat Password',
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Password tidak sama')
        return cd['password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('tanggal_lahir', 'photo')
