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


class Usuario(models.Model):
    celular = models.CharField(max_length=20, null=True)
    primeiro_nome = models.CharField(max_length=50)
    ultimo_nome = models.CharField(max_length=50)
    nome_completo = models.CharField(max_length=50)
    email = models.CharField(max_length=100, null=True)
    user_login_id = models.ForeignKey('auth.User',  on_delete=models.DO_NOTHING, null=True)


class RioUsuario(models.Model):
    usuario = models.ForeignKey('core.Usuario',  on_delete=models.DO_NOTHING, null=True)
    rio = models.ForeignKey('core.Rio',  on_delete=models.DO_NOTHING, null=True)


