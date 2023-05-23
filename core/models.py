from django.db import models

# Create your models here.
class Esp32(models.Model):
    rio = models.ForeignKey('core.Rio',  on_delete=models.DO_NOTHING, null=True)
    latitude = models.IntegerField(null=True)
    longitude = models.IntegerField(null=True)


class Rio(models.Model):
    nome = models.CharField(max_length=100, null=True)
    cidade = models.CharField(max_length=100, null=True)

class MedicoesRio(models.Model):
    esp32_id = models.ForeignKey('core.Esp32',  on_delete=models.DO_NOTHING, null=True)
    altura = models.DecimalField(max_digits=100, decimal_places=3, null=True)
    dat_medicao = models.DateTimeField(null=True)
