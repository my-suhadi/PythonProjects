from django.views.generic import TemplateView

from artikel.views import ArtikelPerKategori


class BlogHomeView(TemplateView, ArtikelPerKategori):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        querysets = self.get_artikel_terakhir_tiap_kategori()
        konteks = {
            'artikel_terakhir': querysets,
        }
        return konteks