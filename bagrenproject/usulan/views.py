from django.shortcuts import render

# Create your views here.

def index(request):
	konteks = {
		'judul':'Usulan',
		'isi':'untuk memasukkan usulan',
	}

	return render(request, 'usulan/index.html', konteks)