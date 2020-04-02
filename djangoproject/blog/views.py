from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView, CreateView

from .models import Artikel
from .forms import ArtikelForm


class ArtikelCreateView2(CreateView):
    model = Artikel
    fields = [
        'judul',
        'isi',
        'penulis',
    ]

    konteks_tambahan = {
        'judul_halaman': 'Tambah artikel model form',
    }

    def get_context_data(self, **kwargs):
        self.kwargs.update(self.konteks_tambahan)

        kwargs = self.kwargs
        return super().get_context_data(**kwargs)


class ArtikelCreateView1(CreateView):
    form_class = ArtikelForm
    template_name = 'blog/create.html'

    konteks_tambahan = {
        'judul_halaman': 'Tambah artikel menggunakan create view',
    }

    def get_context_data(self, **kwargs):
        self.kwargs.update(self.konteks_tambahan)

        kwargs = self.kwargs
        return super().get_context_data(**kwargs)


class ArtikelFormView(FormView):
    form_class = ArtikelForm
    template_name = 'blog/create.html'
    success_url = reverse_lazy('blog:list', kwargs={'penulis': 'all'})
    konteks_tambahan = {
        'judul_halaman': 'Tambah Artikel',
    }

    def get_context_data(self, **kwargs):
        self.kwargs.update(self.konteks_tambahan)
        kwargs = self.kwargs

        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        form.save()

        return super().form_valid(form)


class ArtikelDetailView(DetailView):
    model = Artikel
    tambahan_context = {
        'page_title': 'Detail Artikel'
    }

    def get_context_data(self, **kwargs):
        self.kwargs.update(self.tambahan_context)

        artikel_lain = self.model.objects.exclude(slug=self.kwargs['slug'])
        self.kwargs.update({'artikel_lain': artikel_lain})

        kwargs = self.kwargs
        print(kwargs)

        return super().get_context_data(**kwargs)


class ArtikelListView(ListView):
    model = Artikel
    ordering = ['penulis']
    # paginate_by = 2
    extra_context = {
        'page_title': 'Blog Dengan ListView',
    }

    def get_queryset(self):
        if self.kwargs['penulis'] != 'all':
            self.queryset = self.model.objects.filter(penulis__iexact=self.kwargs['penulis'])
            self.kwargs.update({
                'penulis': self.kwargs['penulis'],
            })
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        self.kwargs.update(self.extra_context)

        kwargs = self.kwargs
        print(self.kwargs)

        return super().get_context_data(**kwargs)


def index(request):
    context = {
        'page_title': 'Blog',
    }

    return render(request, 'blog/index.html', context)
