from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.template import loader
from datetime import datetime
from django.shortcuts import redirect
import array

from pagar.models import Pagar
from receber.models import Receber
from classificacao.models import Classificacao

def mes(data):
    d = data.strftime('%b-%Y')
    return d

def read(request):
    rel = dict()

    p = Pagar.objects.all().values('data_pagamento','classificacao','situacao','transacao','valor','tag')
    r = Receber.objects.all().values('data_recebimento','classificacao','situacao','transacao','valor','tag')
    pare = p.union(r)

    for pr in pare:
        if pr['tag'] == 'P':
            rel['saldo_total'] = 0
            rel[pr['classificacao']] = 0
            rel[pr['situacao']] = 0
            rel[pr['transacao']] = 0

    for pr in pare:
        if pr['tag'] == 'P':
            rel['saldo_total'] -= pr['valor']
        else:
            rel['saldo_total'] += pr['valor']

    template = loader.get_template('fluxo/fluxo.html')
    context ={
        'contas':pare,
        'calculos':rel,
    }
    return HttpResponse(template.render(context,request))