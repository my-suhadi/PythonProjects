from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


# Create your models here.

class MyAkunManager(BaseUserManager):
    # harus meng-overide create_user dan create_superuser

    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Email harus diisi')
        if not username:
            raise ValueError('Username tidak boleh kosong')

        user = self.model(email=self.normalize_email(email), username=username)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(email=self.normalize_email(email), username=username, password=password)

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)


class Akun(AbstractBaseUser):
    # harus meng-overide method has_perm dan has_module_perms
    email = models.EmailField(verbose_name='email', max_length=30, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='tanggal daftar', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='login terakhir', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    akun = MyAkunManager()

    def __str__(self):
        return '{}. {}'.format(self.id, self.email)

    def has_perm(self, perm, obj=None):
        return self.is_admin

    @staticmethod
    def has_module_perms(app_label):
        return True

    class Meta:
        verbose_name_plural = 'Kumpulan akun'
