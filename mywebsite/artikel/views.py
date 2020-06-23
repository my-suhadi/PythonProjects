from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group
from django.shortcuts import render


# Create your views here.

# simple dekorator cek menggunakan fungsi lambda
@user_passes_test(lambda idPengguna: Group.objects.get(name='penulis') in idPengguna.groups.all())
def artikelAddView2(request):
    konteks = {
        'judul_halaman':'Tambah artikel menggunakan lambda',
    }

    return render(request, 'artikel/artikel_add.html', konteks)

# dekorator check
def cekPenulis(idPengguna):
    grup_penulis = Group.objects.get(name='penulis')
    grup_user = idPengguna.groups.all()

    status = grup_penulis in grup_user
    print(status)

    return status


@user_passes_test(cekPenulis)
def artikelAddView(request):
    konteks = {
        'judul_halaman': 'Tambah Artikel View'
    }

    return render(request, 'artikel/artikel_add.html', konteks)


# internal check
def artikelIndexView(request):
    konteks = {
        'judul_halaman': 'Artikel',
    }
    print(Group.objects.get(name='penulis'))
    print(request.user)
    print(request.user.groups.all())

    grup_penulis = Group.objects.get(name='penulis')
    grup_user = request.user.groups.all()

    templete_name = None
    if grup_penulis in grup_user:
        templete_name = 'artikel/index_penulis.html'
    else:
        templete_name = 'artikel/index_pembaca.html'

    return render(request, templete_name, konteks)
