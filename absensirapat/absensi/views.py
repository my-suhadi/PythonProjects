import random
import string

from django.shortcuts import render, redirect

# Create your views here.
from . import forms
from .models import Rapat


def index(request):
    all_rapat = Rapat.objects.all()
    cx = {
        'titleKey': 'Agenda Rapat',
        'allRapatKey': all_rapat
    }

    return render(request, 'absensi/index.html', cx)


def generate_kode():
    letters = string.ascii_letters
    kode = ''.join(random.choice(letters) for i in range(5))
    return kode


def tambah_rapat(request):
    if request.method == 'POST':
        rapat_form = forms.RapatForm(data=request.POST)
        if rapat_form.is_valid():
            rapat = rapat_form.save(commit=False)
            rapat.kode = generate_kode()
            rapat.save()
            return redirect('indexUrl')
    else:
        rapat_form = forms.RapatForm()

    cx = {
        'titleKey': 'Tambah Agenda Rapat',
        'rapatFormKey': rapat_form
    }

    return render(request, 'absensi/tambah-rapat.html', cx)


def ubah_rapat(request, rapat_id):
    rapat_obj = Rapat.objects.get(id=rapat_id)
    rapat_form = forms.RapatForm(instance=rapat_obj)

    if request.method == 'POST':
        rapat_form = forms.RapatForm(request.POST, instance=rapat_obj)
        if rapat_form.is_valid():
            rapat_form.save()
            return redirect('indexUrl')

    cx = {
        'titleKey': 'Ubah Rapat',
        'rapatFormKey': rapat_form
    }
    return render(request, 'absensi/tambah-rapat.html', cx)


def hapus_rapat(request, rapat_id):
    Rapat.objects.filter(id=rapat_id).delete()
    return redirect('indexUrl')
