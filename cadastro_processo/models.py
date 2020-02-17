from django.db import models

class Planilha (models.Model):
    nome = models.CharField(max_length=120, blank=False, null=False)
    cliente = models.CharField(max_length=120, blank=False, null=False)
    arquivo = models.FileField(upload_to='processos.csv' ,blank=False, null=False)
