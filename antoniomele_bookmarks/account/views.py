from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
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
    template_name = 'account/login.html'
    return render(req, template_name, cx)


@login_required
def dashboard(req):
    cx = {'section': 'dashboard'}
    template_name = 'account/dashboard.html'
    return render(req, template_name, cx)
