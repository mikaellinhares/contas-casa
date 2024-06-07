from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.pagina_principal, name='pagina_principal'),
    path('pessoas/', views.pessoas, name='pessoas'),
    path('propriedades/', views.propriedades, name='propriedades'),
    path('propriedades/<int:id_propriedade>', views.propriedade, name='propriedade'),
    # path('metas/', views.metas, name='metas'),
    # path('categorias/', views.categorias, name='categorias'),
    path('despesas', views.despesas, name='despesas'),
    path('despesas/criar', views.criar_despesa, name='criar_despesa'),
    # path('pagamentos/', views.pagamentos, name='pagamentos'),
    # path('rendas/', views.rendas, name='rendas')
]
