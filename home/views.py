from django.shortcuts import render, get_object_or_404
from .models import Categoria, Produto

def index(request):
    categorias = Categoria.objects.all()
    dados = {'categorias': categorias}
    return render(request, 'index.html', dados)

def produtos(request, id):
    produtos = Produto.objects.filter(categoria=id)
    lista_produtos = {'produtos': produtos}
    return render(request, 'produtos.html', lista_produtos)
