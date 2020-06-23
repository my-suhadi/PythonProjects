from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import TemplateView


# === index view menggunakan class based view ===
class IndexView(TemplateView):
    template_name = 'index_anonymous.html'


# === index view menggunakan function based view ===
# view method dengan internal permission check
def index(request):
    konteks = {
        'judul_halaman': 'Beranda',
    }

    print(request.user.is_authenticated)

    # === blok internal permission check ===
    template_name = None
    if request.user.is_authenticated:
        template_name = 'index_user.html'
    else:
        template_name = 'index_anonymous.html'

    return render(request, template_name, konteks)


def loginView(request):
    konteks = {
        'judul_halaman': 'LOGIN',
    }

    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return render(request, 'login.html', konteks)

    if request.method == 'POST':
        print(request.POST)

        uname = request.POST['username']
        passwd = request.POST['password']

        usr = authenticate(request, username=uname, password=passwd)
        print(usr)

        if usr is not None:
            login(request, usr)
            return redirect('index')
        else:
            return redirect('masuk')


# menggunakan dekorator utk masking login
@login_required
def logoutView(request):
    konteks = {
        'judul_halaman': 'Logout',
    }
    if request.method == 'POST':
        print(request.POST)
        if request.POST['keluar'] == 'Ya':
            print('proses logout')
            logout(request)

            return redirect('index')

    return render(request, 'logout.html', konteks)
