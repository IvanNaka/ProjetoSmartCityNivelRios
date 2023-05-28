import datetime

from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
# from forms import SignUpForm


# Create your views here.
from django.views import View

import core.models


class Home(View):
    def get(self, *args, **kwargs):
        a = 2
        return render(self.request, 'base.html', context={'a':a})


class CadastroView(View):
    def get(self, *args, **kwargs):
        form = core.models.SignUpForm()
        return render(self.request, 'cadastro.html', {'form': form})

    def post(self, *args, **kwargs):
        form = core.models.SignUpForm(self.request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            celular = form.cleaned_data['celular']
            primeiro_nome = form.cleaned_data['primeiro_nome']
            ultimo_nome = form.cleaned_data['ultimo_nome']

            usuario = core.models.Usuario()
            usuario.celular = celular
            usuario.primeiro_nome = primeiro_nome
            usuario.ultimo_nome = ultimo_nome
            usuario.nome_completo = primeiro_nome + ultimo_nome
            usuario.email = email
            usuario.save()

            # Crie o usuário Login

            # userlogin = core.models.UsuarioLogin.objects.create_user(username=username, password=password, usuario=usuario)
            userlogin = core.models.UsuarioLogin()
            userlogin.username = email
            userlogin.password = password
            userlogin.usuario = usuario.pk

            # Redirecione para outra página ou faça qualquer outra ação necessária
            return redirect('home')


class EnvioDados(View):
    def post(self, *args, **kwargs):
        try:
            esp32_id = self.request.POST.get('esp32_id')
            sensor_1 = self.request.POST.get('sensor_1') if self.request.POST.get('sensor_1') else None
            sensor_2 = self.request.POST.get('sensor_2') if self.request.POST.get('sensor_2') else None
            sensor_3 = self.request.POST.get('sensor_3') if self.request.POST.get('sensor_3') else None
            sensor_4 = self.request.POST.get('sensor_4') if self.request.POST.get('sensor_4') else None
            sensor_5 = self.request.POST.get('sensor_5') if self.request.POST.get('sensor_5') else None
            sensor_6 = self.request.POST.get('sensor_6') if self.request.POST.get('sensor_6') else None
            sensor_7 = self.request.POST.get('sensor_7') if self.request.POST.get('sensor_7') else None
            sensor_8 = self.request.POST.get('sensor_8') if self.request.POST.get('sensor_8') else None
            sensor_9 = self.request.POST.get('sensor_9') if self.request.POST.get('sensor_9') else None
            sensor_10 = self.request.POST.get('sensor_10') if self.request.POST.get('sensor_10') else None
            sensor_11 = self.request.POST.get('sensor_11') if self.request.POST.get('sensor_11') else None
            sensor_12 = self.request.POST.get('sensor_12') if self.request.POST.get('sensor_12') else None
            sensor_13 = self.request.POST.get('sensor_13') if self.request.POST.get('sensor_13') else None
            sensor_14 = self.request.POST.get('sensor_14') if self.request.POST.get('sensor_14') else None
            sensor_15 = self.request.POST.get('sensor_15') if self.request.POST.get('sensor_15') else None
            sensor_16 = self.request.POST.get('sensor_16') if self.request.POST.get('sensor_16') else None
            sensor_17 = self.request.POST.get('sensor_17') if self.request.POST.get('sensor_17') else None
            sensor_18 = self.request.POST.get('sensor_18') if self.request.POST.get('sensor_18') else None
            sensor_19 = self.request.POST.get('sensor_19') if self.request.POST.get('sensor_19') else None
            sensor_20 = self.request.POST.get('sensor_20') if self.request.POST.get('sensor_20') else None
            altura = (sum(
                sensor_1, sensor_2, sensor_3, sensor_4, sensor_5, sensor_6, sensor_7, sensor_8, sensor_9, sensor_10,
                sensor_11, sensor_12, sensor_13, sensor_14,sensor_15, sensor_16, sensor_17, sensor_18, sensor_19,sensor_20
            ) * 0.20)
            dat_medicao = datetime.datetime.now()
            medicao = core.models.MedicoesRio()
            medicao.altura = altura
            medicao.esp32_id = esp32_id
            medicao.dat_medicao = dat_medicao
            response = {'status': True}
        except:
            response = {'status': False}
        return JsonResponse(response, safe=False)
