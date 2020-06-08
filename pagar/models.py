from django.db import models

class Pagar(models.Model):
	descricao = models.CharField(max_length=200)