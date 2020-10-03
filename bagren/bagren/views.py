from django.shortcuts import render


def index(request):
    konteks = {
        'judul': 'home page',
        'isi': 'ini adalah isi homepage website'
    }

    return render(request, 'index.html', konteks)