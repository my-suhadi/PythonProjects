from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile


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


def daftar(req):
    if req.method == 'POST':
        user_form = UserRegistrationForm(req.POST)
        if user_form.is_valid():
            # buat objek user baru tp tidak dsimpan dlu
            user_baru = user_form.save(commit=False)
            user_baru.set_password(user_form.cleaned_data['passwd'])  # set_password() utk handle hashing
            user_baru.save()

            # membuat profil user
            Profile.objects.create(user=user_baru)

            nama_template = 'account/daftar_selesai.html'
            cx = {
                'userBaruKey': user_baru
            }
            return render(req, nama_template, cx)
    else:
        user_form = UserRegistrationForm()

    nama_template = 'account/daftar.html'
    cx = {
        'userFormKey': user_form
    }
    return render(req, nama_template, cx)

@login_required
def ubah(req):
    if req.method == 'POST':
        user_form = UserEditForm(req.POST, instance=req.user)
        profile_form = ProfileEditForm(req.POST, req.FILES, instance=req.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=req.user)
        profile_form = ProfileEditForm(instance=req.user.profile)

    nama_template = 'account/ubah.html'
    cx = {
        'userFormKey': user_form,
        'profileFormKey': profile_form,
    }
    return render(req, nama_template, cx)
