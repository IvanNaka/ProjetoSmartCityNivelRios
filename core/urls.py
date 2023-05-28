from django.urls import re_path, path, include

from core import views

urlpatterns = [
    re_path(r'^$', views.Home.as_view(), name='home'),
    re_path(r'^envio_dados$', views.EnvioDados.as_view(), name='envio_dados'),
    re_path(r'^cadastro$', views.CadastroView.as_view(), name='cadastro'),
]
