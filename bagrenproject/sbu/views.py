from django.shortcuts import render, redirect

# Create your views here.

from .models import sbu
from .forms import sbuForm


def index(request):
    daftar_sbu = sbu.objects.all()

    konteks = {
        'judul': 'home sbu',
        'daftar_sbu_': daftar_sbu,
    }

    return render(request, 'sbu/index.html', konteks)


def tambah_sbu(request):
    sbu_form = sbuForm(request.POST or None)
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
    sbu.objects.filter(id=delete_id).delete()
    return redirect('sbu:index')
