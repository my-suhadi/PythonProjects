from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from artikel.models import Artikel


class ArtikelPerKategori():
    model = Artikel

    def get_artikel_terakhir_tiap_kategori(self):
        daftar_kategori = self.model.objects.values_list('kategori', flat=True).distinct()
        queryset = []
        for kategori in daftar_kategori:
            artikel = self.model.objects.filter(kategori=kategori).latest('published')
            queryset.append(artikel)

        return queryset


class ArtikelKategoriListView(ListView):
    model = Artikel
    template_name = 'artikel/artikel_kategori_list.html'
    ordering = ['-published']
    context_object_name = 'artikel_kategori'
    paginate_by = 3

    def get_queryset(self):
        self.queryset = self.model.objects.filter(kategori=self.kwargs['kategori'])
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        # perintah distinct() dgunakan agar gk muncul dobel2
        kategori_list = self.model.objects.values_list('kategori', flat=True).distinct().exclude(
            kategori=self.kwargs['kategori'])
        self.kwargs.update({'kategori_list': kategori_list})
        kwargs = self.kwargs
        return super().get_context_data(**kwargs)


class ArtikelListView(ListView):
    model = Artikel
    template_name = 'artikel/artikel_list.html'
    context_object_name = 'artikel_list'  # mengganti nama object
    ordering = ['-published']
    paginate_by = 3

    def get_context_data(self, **kwargs):
        # perintah distinct() dgunakan agar gk muncul dobel2
        kategori_list = self.model.objects.values_list('kategori', flat=True).distinct()
        self.kwargs.update({'kategori_list': kategori_list})
        kwargs = self.kwargs
        return super().get_context_data(**kwargs)


class ArtikelDetailView(DetailView):
    model = Artikel
    template_name = 'artikel/artikel_detail.html'
    context_object_name = 'artikel'

    def get_context_data(self, **kwargs):
        # perintah distinct() dgunakan agar gk muncul dobel2
        kategori_list = self.model.objects.values_list('kategori', flat=True).distinct()
        self.kwargs.update({'kategori_list': kategori_list})

        artikel_serupa = self.model.objects.filter(kategori=self.object.kategori).exclude(id=self.object.id)
        self.kwargs.update({'artikel_serupa': artikel_serupa})

        kwargs = self.kwargs
        return super().get_context_data(**kwargs)
