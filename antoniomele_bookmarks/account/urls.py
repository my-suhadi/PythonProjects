from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, \
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path

from main import settings
from . import views

urlpatterns = [
    # login view halaman 98
    # path('login/', views.user_login, name='loginUrl')
    path('masuk/', LoginView.as_view(), name='login'),
    path('keluar/', LogoutView.as_view(), name='keluarUrl'),
    path('dashboard/', views.dashboard, name='dashboardUrl'),
    # default template_name=password_change_form.html
    path('ganti_password/',
         PasswordChangeView.as_view(template_name='registration/ganti_password_form.html'),
         name='gantiPaswordUrl'),
    # default template_name=password_change_done.html
    path('ganti_password/selesai/',
         PasswordChangeDoneView.as_view(template_name='registration/ganti_password_selesai.html'),
         name='gantiPasswordSelesaiUrl'),
    path('password_reset/', PasswordResetView.as_view(), name='passwordResetUrl'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='resetTokenUrl'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='resetDoneUrl'),
    path('daftar/', views.daftar, name='daftarUrl'),
    path('ubah/', views.ubah, name='ubahUrl'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
