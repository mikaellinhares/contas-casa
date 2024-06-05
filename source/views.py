from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Pessoa, Propriedade, Despesa, Categoria, Pagamento
from datetime import datetime

from django.http import HttpResponsePermanentRedirect
from django.urls import reverse


# Create your views here.
def pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, template_name='pessoas.html', context={'pessoas': pessoas})


def propriedades(request):
    propriedades = Propriedade.objects.all()

    messages.add_message(request, messages.INFO, "Hello world.")

    return render(request, template_name='propriedades.html', context={'propriedades': propriedades})


def propriedade(request, id_propriedade: int):
    request.session['id_propriedade'] = id_propriedade
    propriedade = Propriedade.objects.get(id=id_propriedade)
    return render(request, template_name='propriedade.html', context={'propriedade': propriedade})


def despesas(request):
    id_propriedade = request.session.get('id_propriedade')
    if not id_propriedade:
        return redirect('propriedades')

    despesas = Despesa.objects.all().filter(propriedade=id_propriedade)
    # Pagamentos da despesa: despesa.pagamento_set.all()
    return render(request, template_name='despesas.html', context={'despesas': despesas, 'hoje': datetime.today()})


def criar_despesa(request):
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

        return render(request, template_name='criar_despesa.html', context=context)
    
    elif request.method == 'POST':
        despesa = Despesa(
            propriedade=Propriedade.objects.get(id=request.session.get('id_propriedade')),
            nome=request.POST.get('nome'),
            categoria=Categoria.objects.get(id=request.POST.get('categoria')),
            valor=request.POST.get('valor'),
            data_vencimento=datetime.strptime(request.POST.get('vencimento', ''), '%Y-%m-%d')
        )

        try:
            despesa.save()
            messages.success(request, 'Despesa criada com sucesso!')
        except Exception as error:
            messages.error(request, f'Ocorreu um erro ao criar a despesa:\n{error}')

        if request.POST.get('pagamento'):
            pagamento = Pagamento(
                despesa=despesa,
                pessoa=Pessoa.objects.get(id=request.POST.get('pessoa')),
                valor=request.POST.get('valor'),
                forma_pagamento=request.POST.get('forma_pagamento'),
                descricao='Pagamento Automático',
                data=datetime.now()
            )

            try:
                pagamento.save()
                messages.success(request, 'Pagamento realizado com sucesso!')
            except Exception as error:
                messages.error(request, f'Ocorreu um erro ao tentar realizar o pagamento da despesa:\n{error}')

        return render(request, template_name='criar_despesa.html')