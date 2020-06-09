from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.template import loader
from datetime import datetime
from django.shortcuts import redirect

from .models import Pagar
from classificacao.models import Classificacao
from transacao.models import Transacao
from situacao.models import Situacao

def read(request):
    pagamentos = Pagar.objects.all()
    template = loader.get_template('pagar/index.html')
    context ={
        'pagamentos':pagamentos,
    }
    return HttpResponse(template.render(context,request))
    
def cadastro(request):
    classificacoes = Classificacao.objects.all()
    transacoes = Transacao.objects.all()
    situacoes = Situacao.objects.all()
    template = loader.get_template('pagar/cadastro.html')
    context ={
        'classificacoes':classificacoes,
        'transacoes':transacoes,
        'situacoes':situacoes,
        'rota':'/daminhaconta/pagar/create',
        'completabarraparaupdate':'',
        'acao':"Criar",
    }
    return HttpResponse(template.render(context,request))

def create(request):
    
    dtp = datetime.strptime(request.POST['data_pagamento'], "%d/%m/%Y").date()
    dtv = datetime.strptime(request.POST['data_vencimento'], "%d/%m/%Y").date()

    c = Classificacao.objects.get(id=request.POST['classificacao_id'])
    t = Transacao.objects.get(id=request.POST['transacao_id'])
    s = Situacao.objects.get(id=request.POST['situacao_id'])
    pagar = Pagar(
        descricao=request.POST['descricao'],
        valor=request.POST['valor'],
        data_pagamento=dtp,
        data_vencimento=dtv,
        classificacao=c,
        transacao=t,
        situacao=s,
    )
    pagar.save()
    return redirect('/daminhaconta/pagar/')

def atualizacao(request,id):
    classificacoes = Classificacao.objects.all()
    transacoes = Transacao.objects.all()
    situacoes = Situacao.objects.all()
    pagar = Pagar.objects.get(id=id)
    pagar.data_pagamento = pagar.data_pagamento.strftime("%d/%m/%Y")
    pagar.data_vencimento = pagar.data_vencimento.strftime("%d/%m/%Y")
    template = loader.get_template('pagar/cadastro.html')
    context ={
        'classificacoes':classificacoes,
        'transacoes':transacoes,
        'situacoes':situacoes,
        'rota':'/daminhaconta/pagar/update',
        'acao':"Atualizar",
        'completabarraparaupdate':'/',
        'pagar':pagar

    }
    return HttpResponse(template.render(context,request))

def update(request,id):
    
    dtp = datetime.strptime(request.POST['data_pagamento'], "%d/%m/%Y").date()
    dtv = datetime.strptime(request.POST['data_vencimento'], "%d/%m/%Y").date()

    pagar = Pagar.objects.get(id=id)
    pagar.descricao = request.POST['descricao']
    pagar.classificacao_id = request.POST['classificacao_id']    
    pagar.transacao_id = request.POST['transacao_id']
    pagar.situacao_id = request.POST['situacao_id']
    pagar.valor = request.POST['valor']
    pagar.data_vencimento = dtv
    pagar.data_pagamento = dtp
    pagar.save()
    return redirect('/daminhaconta/pagar/')

def delete(request,id):    	
    pagar = Pagar.objects.get(id=id)
    pagar.delete()		
    return redirect('/daminhaconta/pagar/')

def relatorio(request):
    
    dti = request.POST['data_inicial']
    dtf = request.POST['data_final']
    dtirelatorio = dti
    dtfrelatorio = dtf
    if dti and dtf: 

        dti = request.POST['data_inicial'].split("/")
        dtf = request.POST['data_final'].split("/")
        dti = dti[2]+"-"+dti[1]+"-"+dti[0];
        dtf = dtf[2]+"-"+dtf[1]+"-"+dtf[0];
        pagamentos = Pagar.objects.filter(data_pagamento__range=[dti, dtf])   
    else:
        pagamentos = Pagar.objects.all()

    template = loader.get_template('pagar/relatorio.html')

    context ={
        'pagamentos':pagamentos,
        'data_inicial':dtirelatorio,
        'data_final':dtfrelatorio,
    }
    return HttpResponse(template.render(context,request))
    
