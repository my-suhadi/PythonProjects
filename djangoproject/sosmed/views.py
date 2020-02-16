from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView, RedirectView, View

# Create your views here.

from .models import Instagram
from .forms import InstagramForm

class SosmedSubList:
	def get_list_data(self, get_request):
		if len(get_request) == 0:
			sublist = Instagram.objects.all()
		elif get_request.__contains__('content_filter'):
			sublist = Instagram.objects.filter(content=get_request['content_filter'])
		else:
			sublist = Instagram.objexts.none()

		return sublist

# SosmedSubList ditaro depan biar SosmedSubList.get_list_data() menjadi prioritas
class SosmedListView(SosmedSubList, TemplateView):
	template_name = "sosmed/list.html"

	def get_context_data(self, *args, **kwargs):
		list_akun = self.get_list_data(self.request.GET)
		list_content = Instagram.objects.values_list('content', flat=True).distinct()
		konteks = {
			'page_title':'Sosial media menggunakan class based view',
			'semua_akun':list_akun,
			'list_content':list_content,
		}

		return konteks

class SosmedDeleteView(RedirectView):
	pattern_name = 'sosmed:list'

	def get_redirect_url(self, *args, **kwargs):
		delete_id = kwargs['delete_id']
		Instagram.objects.filter(id=delete_id).delete()
		return super().get_redirect_url()

class SosmedFormView(View):
	template_name = 'sosmed/create.html'
	form = InstagramForm()
	mode = None
	context = None

	def get(self, *args, **kwargs):
		if self.mode == 'update':
			akun_update = Instagram.objects.get(id=kwargs['update_id'])
			data = akun_update.__dict__
			self.form = InstagramForm(initial=data, instance=akun_update)

		self.context = {
			'page_title': 'Tambah akun',
			'akun_form': self.form,
		}

		return render(self.request, self.template_name, self.context)

	def post(self, *args, **kwargs):
		if kwargs.__contains__('update_id'):
			akun_update = Instagram.objects.get(id=kwargs['update_id'])
			self.form = InstagramForm(self.request.POST, instance=akun_update)
		else:
			self.form = InstagramForm(self.request.POST)

		if self.form.is_valid():
			self.form.save()

		return redirect('sosmed:list')