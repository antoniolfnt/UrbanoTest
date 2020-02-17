from django.db import models


# Criação do modelo 'Processo' com os atributos: pasta, comarca e uf. Ambos string.
class Processo(models.Model):
    pasta = models.CharField(max_length=120, blank=False, null=False)
    comarca = models.CharField(max_length=120, blank=False, null=False)
    uf = models.CharField(max_length=120, blank=False, null=False)
