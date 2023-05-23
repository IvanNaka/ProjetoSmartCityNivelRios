import datetime

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View

import core.models


class Home(View):
    def get(self, *args, **kwargs):
        a = 2
        return render(self.request, 'base.html', context={'a':a})


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
            altura = (sum(sensor_1, sensor_2, sensor_3, sensor_4, sensor_5, sensor_6, sensor_7, sensor_8, sensor_9, sensor_10) * 0.20)
            dat_medicao = datetime.datetime.now()
            medicao = core.models.MedicoesRio()
            medicao.altura = altura
            medicao.esp32_id = esp32_id
            medicao.dat_medicao = dat_medicao
            response = {'status': True}
        except:
            response = {'status': False}
        return JsonResponse(response, safe=False)
