from django.db import models
from classificacao.models import Classificacao
from transacao.models import Transacao
from situacao.models import Situacao

class Receber(models.Model):
	data_recebimento = models.DateField(null=True)
	descricao = models.CharField(max_length=200)
	classificacao = models.ForeignKey(Classificacao, on_delete=models.SET_NULL, null = True)
	transacao = models.ForeignKey(Transacao, on_delete=models.SET_NULL, null = True)
	situacao = models.ForeignKey(Situacao, on_delete=models.SET_NULL, null = True)
	valor = models.FloatField(null=True, blank=True, default=None)