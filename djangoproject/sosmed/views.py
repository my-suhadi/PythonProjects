from django.shortcuts import render, redirect

# Create your views here.

from .models import Instagram
from .forms import InstagramForm

def list(request):
	semua_akun_ = Instagram.objects.all()

	konteks = {
		'page_title':'Sosial media',
		'semua_akun':semua_akun_,
	}

	return render(request, 'sosmed/list.html', konteks)

def create(request):
	akun_form_ = InstagramForm(request.POST or None)

	if request.method == 'POST':
		if akun_form_.is_valid():
			akun_form_.save()
		return redirect('sosmed:list')

	konteks = {
		'page_title':'Tambah akun',
		'akun_form':akun_form_,
	}

	return render(request, 'sosmed/create.html', konteks)

def hapus(request, delete_id):
	Instagram.objects.filter(id=delete_id).delete()
	return redirect('sosmed:list')

def ubah(request, update_id):
	akun_update = Instagram.objects.get(id=update_id)

	data = {
		'nama_depan':akun_update.nama_depan,
		'nama_belakang':akun_update.nama_belakang,
		'username':akun_update.username,
	}

	update_form = InstagramForm(request.POST or None, initial=data, instance=akun_update)

	if request.method == 'POST':
		if update_form.is_valid():
			update_form.save()
		return redirect('sosmed:list')
	
	konteks = {
		'page_title':'Update akun',
		'akun_form':update_form,
	}

	return render(request, 'sosmed/create.html', konteks)