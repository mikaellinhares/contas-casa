from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.template.loader import render_to_string
from django.contrib import messages
from django.db import transaction
from .models import Pessoa, Propriedade, Despesa, Categoria, Pagamento
from datetime import datetime
from decimal import Decimal
import json


# Create your views here.
def pagina_principal(request):
    return render(request, template_name='pagina_principal.html')


def pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, template_name='pessoas.html', context={'pessoas': pessoas})


def propriedades(request):
    propriedades = Propriedade.objects.all()
    return render(request, template_name='propriedades.html', context={'propriedades': propriedades})


def propriedade(request, id_propriedade: int):
    request.session['id_propriedade'] = id_propriedade
    propriedade = Propriedade.objects.get(id=id_propriedade)
    return render(request, template_name='propriedade.html', context={'propriedade': propriedade})


def despesas(request):
    id_propriedade = request.session.get('id_propriedade')
    if not id_propriedade:
        return redirect('propriedades')

    categorias = Categoria.objects.all()
    despesas = Despesa.objects.all().filter(propriedade=id_propriedade).order_by('-data_criacao', '-id')
    gasto = Despesa.somar_valores(despesas)
    pago = Despesa.somar_pagamentos(despesas)
    pendente = gasto - pago
    
    context = {
        'categorias': categorias, 
        'despesas': despesas,
        'hoje': datetime.today().date,
        'gasto': gasto,
        'pago': pago,
        'pendente': pendente
    }

    return render(request, template_name='despesas.html', context=context)


def despesa_criar(request):
    if request.method == 'GET':
        hoje = datetime.today().strftime('%Y-%m-%d')
        categorias = Categoria.objects.all()
        pessoas = Propriedade.objects.get(id=request.session['id_propriedade']).pessoas.all()
        formas_pagamento = Pagamento.PAYMENT_METHODS

        context = {
            'hoje': hoje,
            'categorias': categorias,
            'pessoas': pessoas,
            'formas_pagamento': formas_pagamento 
        }

        return render(request, template_name='despesa_criar.html', context=context)
    
    elif request.method == 'POST':
        try:
            despesa = Despesa(
                propriedade=Propriedade.objects.get(id=request.session.get('id_propriedade')),
                nome=request.POST.get('nome'),
                categoria=Categoria.objects.get(id=request.POST.get('categoria')),
                valor=request.POST.get('valor'),
                data_vencimento=datetime.strptime(request.POST.get('vencimento', ''), '%Y-%m-%d')
            )
            despesa.save()
            messages.success(request, 'Despesa criada com sucesso!')
        except Exception as error:
            messages.error(request, f'Ocorreu um erro ao criar a despesa:\n{error}')

        if request.POST.get('pagamento', 'false') == 'true':
            try:
                pessoa = Pessoa.objects.get(id=request.POST.get('pessoa'))
                valor = request.POST.get('valor')

                pagamento = Pagamento(
                    despesa=despesa,
                    pessoa=pessoa,
                    valor=valor,
                    forma_pagamento=request.POST.get('forma_pagamento'),
                    descricao='Pagamento Automático',
                    data=datetime.now()
                )
                pagamento.save()

                pessoa.saldo -= Decimal(valor)
                pessoa.save()

                messages.success(request, 'Pagamento realizado com sucesso!')
                
            except Exception as error:
                messages.error(request, f'Ocorreu um erro ao tentar realizar o pagamento da despesa:\n{error}')
        else:
            messages.error(request, f'Não foi registrado pagamento para a despesa')

        return redirect('despesa_criar')


def despesa_pagamentos(request, despesa_id: int):
    despesa = get_object_or_404(Despesa, id=despesa_id)

    pagamentos = despesa.pagamento_set.all().order_by('-data', '-valor')
    valor_pendente = despesa.valor_pendente()

    context = {
        'despesa_id': despesa.id,
        'pagamentos': pagamentos,
        'valor_pendente': valor_pendente,
        'valor_pendente_str': str(valor_pendente)
    }
    
    if valor_pendente > 0:
        context['categorias'] = Categoria.objects.all()
        context['pessoas'] = Propriedade.objects.get(id=request.session['id_propriedade']).pessoas.all()
        context['formas_pagamento'] = Pagamento.PAYMENT_METHODS
        context['hoje'] = datetime.today().strftime('%Y-%m-%d')

    pagamentos_html = render_to_string('despesa_pagamentos.html', context=context, request=request)

    return JsonResponse(pagamentos_html, safe=False)


@require_POST
def despesa_pagar(request, despesa_id: int):
    try:
        body = json.loads(request.body.decode('utf-8'))

        valor           = body.get('valor')
        forma_pagamento = body.get('forma_pagamento')
        descricao       = body.get('descricao')
        pessoa_id       = body.get('pessoa')
        data_str        = body.get('data')

        despesa         = get_object_or_404(Despesa, id=despesa_id)
        pessoa          = get_object_or_404(Pessoa, id=pessoa_id)
        data            = datetime.strptime(data_str, '%Y-%m-%d')

        with transaction.atomic():
            pagamento = Pagamento(
                despesa=despesa,
                pessoa=pessoa,
                valor=valor,
                forma_pagamento=forma_pagamento,
                descricao=descricao,
                data=data
            )
            pagamento.save()

            pessoa.saldo -= Decimal(valor)
            pessoa.save()

        return HttpResponse(status=201)
    
    except Exception as erro:
        print(erro)
        return HttpResponse(status=400)


def pessoa_rendas(request, pessoa_id: int):
    pessoa = get_object_or_404(Pessoa, id=pessoa_id)

    rendas = pessoa.renda_set.all().order_by('-data', '-valor')

    context = {
        'pessoa_id': pessoa.id,
        'rendas': rendas,
    }

    if request.method == "GET":
        return render(request=request, template_name='components/modal_rendas.html', context=context)
    else:
        rendas_html = render_to_string('components/modal_rendas.html', context=context, request=request)
        return JsonResponse(rendas_html, safe=False)


def pessoa_adicionar_renda(request, pessoa_id: int):
    pessoa = get_object_or_404(Pessoa, id=pessoa_id)
    print(pessoa)
    return ""