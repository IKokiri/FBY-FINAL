from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.template import loader
from datetime import datetime
from django.shortcuts import redirect

from .models import Pagar

def read(request):
    pagamentos = Pagar.objects.all()
    template = loader.get_template('pagar/index.html')
    context ={
        'pagamentos':pagamentos,
    }
    return HttpResponse(template.render(context,request))
    
def cadastro(request):
    template = loader.get_template('pagar/cadastro.html')
    context ={
        'rota':'/daminhaconta/pagar/create',
        'completabarraparaupdate':'',
        'acao':"Criar",
    }
    return HttpResponse(template.render(context,request))

def create(request):
    pagar = Pagar(
        descricao=request.POST['descricao']
    )
    pagar.save()
    return redirect('/daminhaconta/pagar/')

def atualizacao(request,id):

    pagar = Pagar.objects.get(id=id)

    template = loader.get_template('pagar/cadastro.html')
    context ={
        'rota':'/daminhaconta/pagar/update',
        'acao':"Atualizar",
        'completabarraparaupdate':'/',
        'pagar':pagar

    }
    return HttpResponse(template.render(context,request))

def update(request,id):
    pagar = Pagar.objects.get(id=id)
    pagar.descricao = request.POST['descricao']
    pagar.save()
    return redirect('/daminhaconta/pagar/')

def delete(request,id):    	
    pagar = Pagar.objects.get(id=id)
    pagar.delete()		
    return redirect('/daminhaconta/pagar/')

    
