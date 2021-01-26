from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render

# Create your views here.
from .forms import UploadFileForm
from .models import Jabatan, Bagian, Golongan, Pegawai


def index(request):
    return render(request, 'nominatif/index.html', {})


def import_sheet(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)

        def gol_func(row):
            q = Golongan.objects.filter(gol=row[0])[0]
            row[0] = q
            return row

        def jabatan_func(row):
            q = Jabatan.objects.filter(nama=row[0])[0]
            row[0] = q
            return row

        def bagian_func(row):
            q = Bagian.objects.filter(nama=row[0])[0]
            row[0] = q
            return row

        if form.is_valid():
            # Bagian.objects.all().delete()
            request.FILES['file'].save_to_database(
                [Pegawai, Golongan, Jabatan, Bagian],
                [None, gol_func, jabatan_func, bagian_func()],
                [
                    ['nama', 'nip', 'golongan', 'jabatan', 'bagian'],
                    ['gol'],
                    ['jabatan'],
                    ['bagian'],
                ],
                name_columns_by_row=0)
            return redirect('nominatifApp:indexUrl')
        else:
            return HttpResponseBadRequest()
    else:
        form = UploadFileForm()
    return render(request, 'nominatif/upload_form.html',
                  {
                      'formKey': form,
                      'titleKey': 'Import data excel',
                      'headerKey': 'Upload data jabatan',
                  })
