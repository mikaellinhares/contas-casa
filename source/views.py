from django.shortcuts import render
from .models import Pessoa, Propriedade


# Create your views here.
def pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, template_name='pessoas.html', context={'pessoas': pessoas})


def propriedades(request):
    propriedades = Propriedade.objects.all()
    return render(request, template_name='propriedades.html', context={'propriedades': propriedades})
