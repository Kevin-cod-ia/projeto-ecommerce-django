from django.urls import path
from .views import ListaProdutos, DetalhesProduto, AdicionarAoCarrinho, RemoverDoCarrinho, Carrinho, ResumoDaCompra, Busca

app_name = 'produto'

urlpatterns = [
    path('',ListaProdutos.as_view(), name="lista"),
    path('<slug>',DetalhesProduto.as_view(), name="detalhes"),
    path('adicionaraocarrinho/',AdicionarAoCarrinho.as_view(), name="adicionaraocarrinho"),
    path('removerdocarrinho/',RemoverDoCarrinho.as_view(), name="removerdocarrinho"),
    path('carrinho/',Carrinho.as_view(), name="carrinho"),
    path('resumodacompra/',ResumoDaCompra.as_view(), name="resumodacompra"),
    path('busca/',Busca.as_view(), name="busca"),
]
