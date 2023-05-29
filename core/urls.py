from django.urls import re_path, path, include
from django.views.decorators.csrf import csrf_exempt

from core import views

urlpatterns = [
    re_path(r'^$', views.Home.as_view(), name='home'),
    re_path(r'^envio_dados$', csrf_exempt(views.EnvioDados.as_view()), name='envio_dados'),
    re_path(r'^cadastro$', views.CadastroView.as_view(), name='cadastro'),
    re_path(r'^login$', views.LoginView.as_view(), name='cadastro'),
]
