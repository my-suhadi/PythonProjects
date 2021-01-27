import xlsxwriter
from django.core import serializers
from django.http import HttpResponse, JsonResponse

from django.shortcuts import render, redirect
from io import BytesIO

# Create your views here.
from nominatif.models import Pegawai
from . import forms
from .models import Peserta
from absensi.models import Rapat


def index(request, rapat_id):
    all_peserta = Peserta.objects.all().filter(rapat_id=rapat_id)
    cx = {
        'titleKey': 'Daftar Peserta Rapat',
        'rapatIdKey': rapat_id,
        'allPesertaKey': all_peserta
    }

    return render(request, 'peserta/index.html', cx)


def tambah_peserta(request, kode):
    if request.method == 'POST':
        peserta_form = forms.PesertaForm(data=request.POST)
        if peserta_form.is_valid():
            peserta = peserta_form.save(commit=False)
            peserta.rapat_id = Rapat.objects.get(kode=kode)
            peserta.save()
            return render(request, 'peserta/sukses.html', {})
    else:
        peserta_form = forms.PesertaForm()

    cx = {
        'titleKey': 'Tambah Peserta Rapat',
        'pesertaFormKey': peserta_form
    }

    return render(request, 'peserta/tambah-peserta.html', cx)


def export_peserta(request, rapat_id):
    all_peserta = Peserta.objects.all().filter(rapat_id=rapat_id)

    output = BytesIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet()
    columns = (
        'NO.',
        'NAMA',
        'NIP',
        'JABATAN',
        'UNIT KERJA',
    )
    row_num = 0

    for col_num, column_title in enumerate(columns, 0):
        worksheet.write(row_num, col_num, column_title)

    for peserta in all_peserta:
        row_num += 1
        row = (
            row_num,
            peserta.nama,
            peserta.nip,
            peserta.jabatan,
            peserta.unit_kerja,
        )
        for col_num, cell_value in enumerate(row, 0):
            worksheet.write(row_num, col_num, cell_value)

    workbook.close()

    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment;filename="peserta_rapat.xlsx"'
    response.write(output.getvalue())

    return response


def get_data_perserta(request):
    nip_peserta = request.GET.get('nip')
    data_peserta = Pegawai.objects.get(nip=nip_peserta)
    response = {
        'namaKey': data_peserta.nama,
        'jabatanKey': data_peserta.jabatan.nama,
        'bagianKey': data_peserta.bagian.nama,
    }
    print(JsonResponse(response))

    return JsonResponse(response)
