from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.template import loader
from datetime import datetime
from django.shortcuts import redirect

from .models import Situacao

def read(request):
    situacoes = Situacao.objects.all()
    template = loader.get_template('situacao/index.html')
    context ={
        'situacoes':situacoes,
    }
    return HttpResponse(template.render(context,request))
    
def cadastro(request):
    template = loader.get_template('situacao/cadastro.html')
    context ={
        'rota':'/daminhaconta/situacao/create',
        'completabarraparaupdate':'',
        'acao':"Criar",
    }
    return HttpResponse(template.render(context,request))

def create(request):
    situacao = Situacao(
        situacao=request.POST['situacao']
    )
    situacao.save()
    return redirect('/daminhaconta/situacao/')

def atualizacao(request,id):

    situacao = Situacao.objects.get(id=id)

    template = loader.get_template('situacao/cadastro.html')
    context ={
        'rota':'/daminhaconta/situacao/update',
        'acao':"Atualizar",
        'completabarraparaupdate':'/',
        'situacao':situacao

    }
    return HttpResponse(template.render(context,request))

def update(request,id):
    situacao = Situacao.objects.get(id=id)
    situacao.situacao = request.POST['situacao']
    situacao.save()
    return redirect('/daminhaconta/situacao/')

def delete(request,id):    	
    situacao = Situacao.objects.get(id=id)
    situacao.delete()		
    return redirect('/daminhaconta/situacao/')

    
