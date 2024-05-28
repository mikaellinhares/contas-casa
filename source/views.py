from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Pessoa, Propriedade, Despesa
from datetime import datetime


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