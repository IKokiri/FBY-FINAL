from django.db import models

class Receber(models.Model):
	descricao = models.CharField(max_length=200)