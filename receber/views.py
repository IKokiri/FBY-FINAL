from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.template import loader
from datetime import datetime
from django.shortcuts import redirect

from .models import Receber

def read(request):
    recebimentos = Receber.objects.all()
    template = loader.get_template('receber/index.html')
    context ={
        'recebimentos':recebimentos,
    }
    return HttpResponse(template.render(context,request))
    
def cadastro(request):
    template = loader.get_template('receber/cadastro.html')
    context ={
        'rota':'/daminhaconta/receber/create',
        'completabarraparaupdate':'',
        'acao':"Criar",
    }
    return HttpResponse(template.render(context,request))

def create(request):
    receber = Receber(
        descricao=request.POST['descricao']
    )
    receber.save()
    return redirect('/daminhaconta/receber/')

def atualizacao(request,id):

    receber = Receber.objects.get(id=id)

    template = loader.get_template('receber/cadastro.html')
    context ={
        'rota':'/daminhaconta/receber/update',
        'acao':"Atualizar",
        'completabarraparaupdate':'/',
        'receber':receber

    }
    return HttpResponse(template.render(context,request))

def update(request,id):
    receber = Receber.objects.get(id=id)
    receber.descricao = request.POST['descricao']
    receber.save()
    return redirect('/daminhaconta/receber/')

def delete(request,id):    	
    receber = Receber.objects.get(id=id)
    receber.delete()		
    return redirect('/daminhaconta/receber/')

    
