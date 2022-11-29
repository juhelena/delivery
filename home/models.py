from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    celular = models.CharField(max_length=11) 
    email = models.EmailField(max_length=50)   

class Endereco(models.Model):
    rua = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    numero = models.CharField(max_length=5)
    cep = models.CharField(max_length=15)
       
class Categoria(models.Model):
    categoria = models.CharField(max_length=50)
    imagem = models.ImageField()

    def __str__(self) -> str:
        return self.categoria
       
class Produto(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    categoria = models.ForeignKey(Categoria,on_delete=models.PROTECT)
    imagem = models.ImageField()

    def __str__(self) -> str:
        return self.titulo
    
class Pedido(models.Model):
    pagamento_dinheiro = 'D'
    pagamento_cartao = 'C'
    pagamento_pix = 'P'
    
    formas_pagamento = [(pagamento_dinheiro, 'Dinheiro'), (pagamento_cartao, 'Cartão'), (pagamento_pix, 'Pix')]
    pagamento = models.CharField(max_length=1, choices=formas_pagamento)
    
    preco = models.DecimalField(max_digits=5, decimal_places=2)
    
    