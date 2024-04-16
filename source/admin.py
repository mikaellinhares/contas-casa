from .models import Propriedade, Pessoa, Renda, Meta, Categoria, Despesa, Pagamento
from django.contrib import admin


admin.site.register(Propriedade)
admin.site.register(Pessoa)
admin.site.register(Renda)
admin.site.register(Meta)
admin.site.register(Categoria)
admin.site.register(Despesa)
admin.site.register(Pagamento)
