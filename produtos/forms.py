from django.forms import ModelForm
from .models import Produto, Cliente, Venda

class ProdutoForm(ModelForm):
    class Meta: # armazena metadados
        model = Produto
        fields = ['nome', 'descricao', 'preco', 'estoque']

class ClienteForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'data_nascimento']

class VendaForm(ModelForm):
    class Meta:
        model = Venda
        fields = ['cliente', 'produto', 'quantidade', 'data_venda']