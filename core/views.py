import datetime
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db.models import F
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm, RiosForm
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Create your views here.
from django.views import View

import core.models


class Home(View):
    def get(self, *args, **kwargs):
        ls_esps = list(core.models.Esp32.objects.values('id'))
        qtd_rios_acima = 0
        qtd_rios_abaixo = 0
        infos_rios = []
        for esp in ls_esps:
            dados_rio = core.models.MedicoesRio.objects.values(
                'esp32_id', 'altura', 'dat_medicao', nm_rio=F('esp32_id__rio__nome')
            ).filter(esp32_id=esp['id']).order_by('-dat_medicao').first()
            infos_rios.append(dados_rio)
        for esp in ls_esps:
            altura = core.models.MedicoesRio.objects.values_list('altura', flat=True).filter(esp32_id=esp['id']).order_by('-dat_medicao').first()
            if altura >= 2:
                qtd_rios_acima = qtd_rios_acima + 1
            elif altura <= 1:
                qtd_rios_abaixo = qtd_rios_abaixo + 1
        context = {
            'infos_rios': infos_rios,
            'qtd_rios_acima': qtd_rios_acima,
            'qtd_rios_abaixo': qtd_rios_abaixo
        }

        return render(self.request, 'base.html', context=context)


class CadastroView(View):
    def get(self, *args, **kwargs):
        form = SignUpForm()
        return render(self.request, 'cadastro.html', {'form': form})

    def post(self, *args, **kwargs):
        form = SignUpForm(self.request.POST)

        if form.is_valid():
            # username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            celular = form.cleaned_data['celular']
            primeiro_nome = form.cleaned_data['primeiro_nome']
            ultimo_nome = form.cleaned_data['ultimo_nome']

            # Crie o usuário Login
            try:
                userlogin = User.objects.create_user(username=email, email=email, password=password)
                usuario = core.models.Usuario()
                usuario.celular = celular
                usuario.primeiro_nome = primeiro_nome
                usuario.ultimo_nome = ultimo_nome
                usuario.nome_completo = primeiro_nome + ultimo_nome
                usuario.email = email
                usuario.user_login_id = userlogin
                usuario.save()

            except:
                return JsonResponse(data={'status': False, 'descricao': 'Erro ao cadastrar, verificar dados inseridos'}, safe=False)

            # Redirecione para outra página ou faça qualquer outra ação necessária
            return redirect('home')
        else:
            return JsonResponse(dict={'status':False}, safe=False)


class LoginView(View):
    def get(self, *args, **kwargs):
        form = LoginForm()
        return render(self.request, 'login.html', {'form': form})

    def post(self, *args, **kwargs):
        form = LoginForm(self.request.POST)
        if form.is_valid():
            if form.is_valid():
                username = form.cleaned_data['email']
                password = form.cleaned_data['password']

                # Autentique o usuário
                user = authenticate(username=username, password=password)

                if user is not None:
                    # Faça o login do usuário
                    login(self.request, user)

                    # Redirecione para outra página ou faça qualquer outra ação necessária
                    return redirect('home')
                else:
                    # Trate o caso em que a autenticação falhou
                    form.add_error(None, 'Usuário ou senha inválidos.')
                    return JsonResponse(data={'status': False, 'descricao': 'Usuário ou senha inválidos.'}, safe=False)
        else:
            return JsonResponse(data={'status': False}, safe=False)

class RiosUsuarioView(View):
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            form = RiosForm()
            return render(self.request, 'rios.html', {'form': form})
        else:
            return redirect('login')

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            form = RiosForm(self.request.POST)
            if form.is_valid():
                rios_form = form.cleaned_data.get("rios_field")
                user_obj = core.models.Usuario.objects.filter(email=self.request.user.email).first()
                core.models.RioUsuario.objects.filter(usuario=user_obj).delete()
                for rio in rios_form:
                    rio_obj = core.models.Rio.objects.filter(id=rio).first()
                    rio_usuario = core.models.RioUsuario()
                    rio_usuario.rio = rio_obj
                    rio_usuario.usuario = user_obj
                    rio_usuario.save()
                return redirect('home')
            else:
                return JsonResponse(data={'status': False}, safe=False)
        else:
            return redirect('login')


class EnvioDados(View):
    def post(self, *args, **kwargs):
        try:
            esp32_id = self.request.GET.get('esp32_id')
            sensor_1 = int(self.request.GET.get('sensor_1')) if self.request.GET.get('sensor_1') else None
            sensor_2 = int(self.request.GET.get('sensor_2')) if self.request.GET.get('sensor_2') else None
            sensor_3 = int(self.request.GET.get('sensor_3')) if self.request.GET.get('sensor_3') else None
            sensor_4 = int(self.request.GET.get('sensor_4')) if self.request.GET.get('sensor_4') else None
            sensor_5 = int(self.request.GET.get('sensor_5')) if self.request.GET.get('sensor_5') else None
            sensor_6 = int(self.request.GET.get('sensor_6')) if self.request.GET.get('sensor_6') else None
            sensor_7 = int(self.request.GET.get('sensor_7')) if self.request.GET.get('sensor_7') else None
            sensor_8 = int(self.request.GET.get('sensor_8')) if self.request.GET.get('sensor_8') else None
            sensor_9 = int(self.request.GET.get('sensor_9')) if self.request.GET.get('sensor_9') else None
            sensor_10 = int(self.request.GET.get('sensor_10')) if self.request.GET.get('sensor_10') else None
            sensor_11 = int(self.request.GET.get('sensor_11')) if self.request.GET.get('sensor_11') else None
            sensor_12 = int(self.request.GET.get('sensor_12')) if self.request.GET.get('sensor_12') else None
            sensor_13 = int(self.request.GET.get('sensor_13')) if self.request.GET.get('sensor_13') else None
            sensor_14 = int(self.request.GET.get('sensor_14')) if self.request.GET.get('sensor_14') else None
            sensor_15 = int(self.request.GET.get('sensor_15')) if self.request.GET.get('sensor_15') else None
            sensor_16 = int(self.request.GET.get('sensor_16')) if self.request.GET.get('sensor_16') else None
            sensor_17 = int(self.request.GET.get('sensor_17')) if self.request.GET.get('sensor_17') else None
            sensor_18 = int(self.request.GET.get('sensor_18')) if self.request.GET.get('sensor_18') else None
            sensor_19 = int(self.request.GET.get('sensor_19')) if self.request.GET.get('sensor_19') else None
            sensor_20 = int(self.request.GET.get('sensor_20'))if self.request.GET.get('sensor_20') else None
            altura = ((
                sensor_1 + sensor_2 + sensor_3 + sensor_4 + sensor_5 + sensor_6 + sensor_7 + sensor_8 + sensor_9 +
                sensor_10 + sensor_11 + sensor_12 + sensor_13 + sensor_14 + sensor_15 + sensor_16 + sensor_17
                + sensor_18 + sensor_19 + sensor_20) * 0.20)
            esp32_id = core.models.Esp32.objects.filter(id=esp32_id).first()
            dat_medicao = datetime.datetime.now()
            medicao = core.models.MedicoesRio()
            medicao.altura = altura
            medicao.esp32_id = esp32_id
            medicao.dat_medicao = dat_medicao
            medicao.save()
            if altura >= 2:
                ls_usuarios_cadastrados = list(core.models.RioUsuario.objects.filter(rio_id=esp32_id.rio_id).values_list('usuario__email', flat=True))
                for usuario in ls_usuarios_cadastrados:
                    smtp_server = 'smtp.gmail.com'
                    smtp_port = 587
                    sender_email = 'ivan.nakatani@gmail.com'
                    sender_password = 'rzcyvhigaxgaqdsw'
                    recipient_email = usuario
                    email_subject = f'Risco de alagamento no {esp32_id.rio.nome}'
                    email_body = f'Atenção! Foi detectado altos níveis de água no {esp32_id.rio.nome}, mantenha-se alerta para o risco de alamentos!'
                    message = MIMEMultipart()
                    message['From'] = sender_email
                    message['To'] = recipient_email
                    message['Subject'] = email_subject
                    message.attach(MIMEText(email_body, 'plain'))
                    server = smtplib.SMTP(smtp_server, smtp_port)
                    server.starttls()
                    server.login(sender_email, sender_password)
                    server.send_message(message)
                    server.quit()
            response = {'status': True}
        except Exception as e:
            response = {'status': False, 'descricao': [esp32_id, sensor_1]}
        return JsonResponse(response, safe=False)


    def enviar_email(self, email, rio):
        pass