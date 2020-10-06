from django.shortcuts import render, redirect

# Create your views here.
from sbu.form import SbuForm
from sbu.models import Sbu


def index(request):
    daftar_sbu = Sbu.objects.all()

    konteks = {
        'judul': 'home sbu',
        'daftar_sbu_': daftar_sbu,
    }

    return render(request, 'sbu/index.html', konteks)


def tambah_sbu(request):
    sbu_form = SbuForm(request.POST or None)
    if request.method == 'POST':
        if sbu_form.is_valid():
            sbu_form.save()
        return redirect('sbu:index')

    konteks = {
        'judul': 'tambah sbu',
        'sbu_form_': sbu_form,
    }

    return render(request, 'sbu/tambah.html', konteks)


def hapus_sbu(request, delete_id):
    Sbu.objects.filter(sbu_id=delete_id).delete()
    return redirect('sbu:index')
