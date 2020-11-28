from django.shortcuts import render

# Create your views here.
from absensi import forms
from absensi.models import Rapat


def index(request):
    all_rapat = Rapat.objects.all()
    cx = {
        'titleKey': 'Agenda Rapat',
        'allRapatKey': all_rapat
    }

    return render(request, 'absensi/index.html', cx)

def tambah_rapat(request):
    if request.method == 'POST':
        rapat_form = forms.RapatForm()
    else:
        rapat_form = forms.RapatForm()

    cx = {
        'titleKey': 'Tambah Agenda Rapat',
        'rapatFormKey': rapat_form
    }

    return render(request, 'absensi/tambah-rapat.html', cx)
