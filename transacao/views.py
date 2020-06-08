from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.template import loader
from datetime import datetime
from django.shortcuts import redirect

from .models import Transacao

def read(request):
    transacoes = Transacao.objects.all()
    template = loader.get_template('transacao/index.html')
    context ={
        'transacoes':transacoes,
    }
    return HttpResponse(template.render(context,request))
    
def cadastro(request):
    template = loader.get_template('transacao/cadastro.html')
    context ={
        'rota':'/daminhaconta/transacao/create',
        'completabarraparaupdate':'',
        'acao':"Criar",
    }
    return HttpResponse(template.render(context,request))

def create(request):
    transacao = Transacao(
        transacao=request.POST['transacao']
    )
    transacao.save()
    return redirect('/daminhaconta/transacao/')

def atualizacao(request,id):

    transacao = Transacao.objects.get(id=id)

    template = loader.get_template('transacao/cadastro.html')
    context ={
        'rota':'/daminhaconta/transacao/update',
        'acao':"Atualizar",
        'completabarraparaupdate':'/',
        'transacao':transacao

    }
    return HttpResponse(template.render(context,request))

def update(request,id):
    transacao = Transacao.objects.get(id=id)
    transacao.transacao = request.POST['transacao']
    transacao.save()
    return redirect('/daminhaconta/transacao/')

def delete(request,id):    	
    transacao = Transacao.objects.get(id=id)
    transacao.delete()		
    return redirect('/daminhaconta/transacao/')

    
