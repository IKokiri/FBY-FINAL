from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.template import loader
from datetime import datetime
from django.shortcuts import redirect

from .models import Receber
from classificacao.models import Classificacao
from transacao.models import Transacao
from situacao.models import Situacao

def read(request):
    recebimentos = Receber.objects.all()
    template = loader.get_template('receber/index.html')
    context ={
        'recebimentos':recebimentos,
    }
    return HttpResponse(template.render(context,request))
    
def cadastro(request):
    classificacoes = Classificacao.objects.all()
    transacoes = Transacao.objects.all()
    situacoes = Situacao.objects.all()
    template = loader.get_template('receber/cadastro.html')
    context ={
        'classificacoes':classificacoes,
        'transacoes':transacoes,
        'situacoes':situacoes,
        'rota':'/daminhaconta/receber/create',
        'completabarraparaupdate':'',
        'acao':"Criar",
    }
    return HttpResponse(template.render(context,request))

def create(request):
    
    dtr = datetime.strptime(request.POST['data_recebimento'], "%d/%m/%Y").date()

    c = Classificacao.objects.get(id=request.POST['classificacao_id'])
    t = Transacao.objects.get(id=request.POST['transacao_id'])
    s = Situacao.objects.get(id=request.POST['situacao_id'])
    receber = Receber(
        descricao=request.POST['descricao'],
        valor=request.POST['valor'],
        data_recebimento=dtr,
        classificacao=c,
        transacao=t,
        situacao=s,
    )
    receber.save()
    return redirect('/daminhaconta/receber/')

def atualizacao(request,id):
    classificacoes = Classificacao.objects.all()
    transacoes = Transacao.objects.all()
    situacoes = Situacao.objects.all()
    receber = Receber.objects.get(id=id)
    receber.data_recebimento = receber.data_recebimento.strftime("%d/%m/%Y")
    template = loader.get_template('receber/cadastro.html')
    context ={
        'classificacoes':classificacoes,
        'transacoes':transacoes,
        'situacoes':situacoes,
        'rota':'/daminhaconta/receber/update',
        'acao':"Atualizar",
        'completabarraparaupdate':'/',
        'receber':receber

    }
    return HttpResponse(template.render(context,request))

def update(request,id):
    
    dtr = datetime.strptime(request.POST['data_recebimento'], "%d/%m/%Y").date()

    receber = Receber.objects.get(id=id)
    receber.descricao = request.POST['descricao']
    receber.classificacao_id = request.POST['classificacao_id']    
    receber.transacao_id = request.POST['transacao_id']
    receber.situacao_id = request.POST['situacao_id']
    receber.valor = request.POST['valor']
    receber.data_recebimento = dtr
    receber.save()
    return redirect('/daminhaconta/receber/')

def delete(request,id):    	
    receber = Receber.objects.get(id=id)
    receber.delete()		
    return redirect('/daminhaconta/receber/')


def relatorio(request):

    template = loader.get_template('receber/relatorio.html')    

    if request.POST:
        if request.POST['data_inicial'] and request.POST['data_final']:
            dti = request.POST['data_inicial']
            dtf = request.POST['data_final']
            dtirelatorio = dti
            dtfrelatorio = dtf

            dti = request.POST['data_inicial'].split("/")
            dtf = request.POST['data_final'].split("/")
            dti = dti[2]+"-"+dti[1]+"-"+dti[0]
            dtf = dtf[2]+"-"+dtf[1]+"-"+dtf[0]
            recebimentos = Receber.objects.filter(data_recebimento__range=[dti, dtf])   

            context ={
                'recebimentos':recebimentos,
                'data_inicial':dtirelatorio,
                'data_final':dtfrelatorio,
            }
            return HttpResponse(template.render(context,request))
    
    recebimentos = Receber.objects.all()
    context ={
        'recebimentos':recebimentos,
    }
    return HttpResponse(template.render(context,request))
    
