from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .forms import LoginForm


def user_login(req):
    if req.method == 'POST':
        form = LoginForm(req.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(req,
                                username=cd['uname'],
                                password=cd['passwd'])
            if user is not None:
                if user.is_active:
                    login(req, user)
                    return HttpResponse('Sukses')
                else:
                    return HttpResponse('Akun non-aktif')
            else:
                return HttpResponse('Login salah')
    else:
        form = LoginForm()
    cx = {
        'formKey': form
    }
    return render(req, 'account/login.html', cx)
