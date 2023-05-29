import uuid

from django import forms
from django.contrib import auth
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import User, AbstractUser, PermissionsMixin, Group, Permission, UserManager
from django.db import models
import django.forms

# Create your models here.
from django.utils.translation import gettext_lazy as _



class Esp32(models.Model):
    rio = models.ForeignKey('core.Rio',  on_delete=models.DO_NOTHING, null=True)
    latitude = models.DecimalField(max_digits=100, decimal_places=6, null=True)
    longitude = models.DecimalField(max_digits=100, decimal_places=6, null=True)


class Rio(models.Model):
    nome = models.CharField(max_length=100, null=True)
    cidade = models.CharField(max_length=100, null=True)


class MedicoesRio(models.Model):
    esp32_id = models.ForeignKey('core.Esp32',  on_delete=models.DO_NOTHING, null=True)
    altura = models.DecimalField(max_digits=100, decimal_places=3, null=True)
    dat_medicao = models.DateTimeField(null=True)


# class UsuarioLogin(AbstractBaseUser, PermissionsMixin):
#
#     usuario = models.OneToOneField('core.Usuario', on_delete=models.DO_NOTHING, null=True)
#     username = models.CharField(max_length=200, unique=True)
#     USERNAME_FIELD = 'username'
#     hash = models.UUIDField(null=True, default=uuid.uuid4)
#     email = models.EmailField(_("email address"), blank=True)
#
#     objects = UserManager()
#
#
#     is_staff = models.BooleanField(
#         _("staff status"),
#         default=False,
#         help_text=_("Designates whether the user can log into this admin site."),
#     )
#     is_superuser = models.BooleanField(
#         _('superuser status'),
#         default=False,
#         help_text=_(
#             'Designates that this user has all permissions without '
#             'explicitly assigning them.'
#         ),
#     )
#     groups = models.ManyToManyField(
#         Group,
#         verbose_name=_('groups'),
#         blank=True,
#         help_text=_(
#             'The groups this user belongs to. A user will get all permissions '
#             'granted to each of their groups.'
#         ),
#         related_name="%(app_label)s_%(class)s_user_set",
#         related_query_name="user",
#     )
#     user_permissions = models.ManyToManyField(
#         Permission,
#         verbose_name=_('user permissions'),
#         blank=True,
#         help_text=_('Specific permissions for this user.'),
#         related_name="%(app_label)s_%(class)s_user_set",
#         related_query_name="user",
#     )


class Usuario(models.Model):
    celular = models.CharField(max_length=20, null=True)
    primeiro_nome = models.CharField(max_length=50)
    ultimo_nome = models.CharField(max_length=50)
    nome_completo = models.CharField(max_length=50)
    email = models.CharField(max_length=100, null=True)
    user_login_id = models.ForeignKey('auth.User',  on_delete=models.DO_NOTHING, null=True)


