from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.template import loader
from datetime import datetime
from django.shortcuts import redirect

from .models import Classificacao

def read(request):
    situacoes = Classificacao.objects.all()
    template = loader.get_template('classificacao/index.html')
    context ={
        'classificacoes':situacoes,
    }
    return HttpResponse(template.render(context,request))
    
def cadastro(request):
    template = loader.get_template('classificacao/cadastro.html')
    context ={
        'rota':'/daminhaconta/classificacao/create',
        'completabarraparaupdate':'',
        'acao':"Criar",
    }
    return HttpResponse(template.render(context,request))

def create(request):
    classificacao = Classificacao(
        classificacao=request.POST['classificacao']
    )
    classificacao.save()
    return redirect('/daminhaconta/classificacao/')

def atualizacao(request,id):

    classificacao = Classificacao.objects.get(id=id)

    template = loader.get_template('classificacao/cadastro.html')
    context ={
        'rota':'/daminhaconta/classificacao/update',
        'acao':"Atualizar",
        'completabarraparaupdate':'/',
        'classificacao':classificacao

    }
    return HttpResponse(template.render(context,request))

def update(request,id):
    classificacao = Classificacao.objects.get(id=id)
    classificacao.classificacao = request.POST['classificacao']
    classificacao.save()
    return redirect('/daminhaconta/classificacao/')

def delete(request,id):    	
    classificacao = Classificacao.objects.get(id=id)
    classificacao.delete()		
    return redirect('/daminhaconta/classificacao/')

    
