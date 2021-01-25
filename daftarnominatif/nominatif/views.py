from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render

# Create your views here.
from .forms import UploadFileForm
from .models import Jabatan


def index(request):
    return render(request, 'index.html', {})


def import_sheet(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # Jabatan.objects.all().delete()
            request.FILES['file'].save_to_database(Jabatan, None, ['nama'],
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
