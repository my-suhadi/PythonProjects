from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render

# Create your views here.
from .forms import UploadFileForm
from .models import Golongan, Pegawai


def index(request):
    return render(request, 'index.html', {})


def import_sheet(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)

        def cust_func(row):
            q = Golongan.objects.filter(gol=row[2])[0]
            row[2] = q
            print(row)
            return row

        if form.is_valid():
            Pegawai.objects.all().delete()
            request.FILES['file'].save_to_database(
                Pegawai,
                cust_func,
                ['nama', 'nip', 'golongan'],
                name_columns_by_row=0)
            return HttpResponse('OK')
        else:
            return HttpResponseBadRequest()
    else:
        form = UploadFileForm()
    return render(request, 'upload_form.html',
                  {
                      'form': form,
                      'title': 'Import data excel',
                      'header': 'Upload data jabatan',
                  })
