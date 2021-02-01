from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import redirect

# Create your views here.
from django.http import HttpResponseBadRequest
from django.shortcuts import render

# Create your views here.
from .forms import UploadFileForm
from .models import Jabatan, Bagian, Golongan, Pegawai


@login_required
def index(request):
    all_pegawai = Pegawai.objects.all()
    paginator = Paginator(all_pegawai, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    cx = {
        'titleKey': 'Daftar Nominatif',
        'allPegawaiKey': all_pegawai,
        'pageKey': page_obj,
    }
    return render(request, 'nominatif/index.html', cx)


@login_required
def import_sheet(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)

        def pegawai_func(row):
            try:
                golongan_row = Golongan.objects.filter(gol=row[2])[0]
                jabatan_row = Jabatan.objects.filter(nama=row[3])[0]
                bagian_row = Bagian.objects.filter(nama=row[4])[0]
            except IndexError:
                golongan_row = Golongan(gol=row[2])
                golongan_row.save()
                jabatan_row = Jabatan(nama=row[3])
                jabatan_row.save()
                bagian_row = Bagian(nama=row[4])
                bagian_row.save()
            row[2] = golongan_row
            row[3] = jabatan_row
            row[4] = bagian_row
            return row

        if form.is_valid():
            Pegawai.objects.all().delete()
            # request.FILES['file'].save_to_database(Jabatan, None, ['nama'], name_columns_by_row=0)
            request.FILES['file'].save_to_database(
                Pegawai,
                pegawai_func,
                ['nama', 'nip', 'golongan', 'jabatan', 'bagian'],
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
                      'headerKey': 'Upload Daftar Pegawai',
                  })
