from django.contrib import admin
from .models import Produto, Cliente, Venda

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'preco', 'estoque')

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'data_nascimento')

@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'produto', 'quantidade', 'data_venda')