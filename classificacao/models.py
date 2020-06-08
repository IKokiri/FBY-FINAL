from django.db import models

class Classificacao(models.Model):
	classificacao = models.CharField(max_length=200)