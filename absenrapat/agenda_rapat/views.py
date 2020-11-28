from django.shortcuts import render


# Create your views here.
from agenda_rapat.models import AgendaRapat


def index(request):
    all_agenda = AgendaRapat.objects.all()

    cx = {
        'judulKey': 'Judul',
        'allAgendaKey': all_agenda,
    }

    return render(request, 'agenda_rapat/index.html', cx)
