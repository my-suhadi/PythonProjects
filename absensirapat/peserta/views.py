from django.shortcuts import render, redirect

# Create your views here.
from . import forms
from .models import Peserta


def index(request, rapat_id):
    all_peserta = Peserta.objects.all().filter(rapat_id=rapat_id)
    cx = {
        'titleKey': 'Daftar Peserta Rapat',
        'allPesertaKey': all_peserta
    }

    return render(request, 'peserta/index.html', cx)


def tambah_peserta(request, rapat_id):
    if request.method == 'POST':
        peserta_form = forms.PesertaForm(data=request.POST)
        if peserta_form.is_valid():
            peserta_form.save()
            return redirect('indexUrl')
    else:
        peserta_form = forms.PesertaForm()

    cx = {
        'titleKey': 'Tambah Peserta Rapat',
        'pesertaFormKey': peserta_form
    }

    return render(request, 'peserta/tambah-peserta.html', cx)
