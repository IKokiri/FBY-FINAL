from django.db import models

class Transacao(models.Model):
	transacao = models.CharField(max_length=200)