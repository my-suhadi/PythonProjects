from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import TemplateView


# === index view menggunakan class based view ===
class IndexView(TemplateView):
    template_name = 'index.html'


# === index view menggunakan function based view ===
def index(request):
    konteks = {
        'judul_halaman': 'Beranda',
    }

    return render(request, 'index.html', konteks)


def loginView(request):
    konteks = {
        'judul_halaman': 'LOGIN',
    }

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

    return render(request, 'login.html', konteks)


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
