from django.contrib import admin
from .models import Cliente, Endereco, Categoria, Produto, Pedido

class ClientesDisplay(admin.ModelAdmin):
    list_display = ('id',  'nome',)

class EnderecosDisplay(admin.ModelAdmin):
    list_display = ('rua',  'bairro',)
    
class CategoriasDisplay(admin.ModelAdmin):
    list_display = ('categoria',)
    
class ProdutosDisplay(admin.ModelAdmin):
    list_display = ('titulo',  'descricao', 'preco',)
    
class PedidosDisplay(admin.ModelAdmin):
    list_display = ('pagamento',  'preco',)
    
admin.site.register(Cliente, ClientesDisplay)
admin.site.register(Endereco, EnderecosDisplay)
admin.site.register(Categoria, CategoriasDisplay)
admin.site.register(Produto, ProdutosDisplay)
admin.site.register(Pedido, PedidosDisplay)

