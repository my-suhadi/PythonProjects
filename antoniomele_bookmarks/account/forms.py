from django import forms


class LoginForm(forms.Form):
    uname = forms.CharField()
    passwd = forms.CharField(widget=forms.PasswordInput)
