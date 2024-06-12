from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Pessoa, Propriedade, Despesa, Categoria, Pagamento
from datetime import datetime

from django.http import HttpResponsePermanentRedirect
from django.urls import reverse


# Create your views here.
def pagina_principal(request):
    return render(request, template_name='pagina_principal.html')


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

    categorias = Categoria.objects.all()
    despesas = Despesa.objects.all().filter(propriedade=id_propriedade)
    
    context = {'categorias': categorias, 'despesas': despesas, 'hoje': datetime.today().date}

    return render(request, template_name='despesas.html', context=context)


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
                pagamento = Pagamento(
                    despesa=despesa,
                    pessoa=Pessoa.objects.get(id=request.POST.get('pessoa')),
                    valor=request.POST.get('valor'),
                    forma_pagamento=request.POST.get('forma_pagamento'),
                    descricao='Pagamento Automático',
                    data=datetime.now()
                )
                pagamento.save()
                messages.success(request, 'Pagamento realizado com sucesso!')
            except Exception as error:
                messages.error(request, f'Ocorreu um erro ao tentar realizar o pagamento da despesa:\n{error}')

        return render(request, template_name='criar_despesa.html')