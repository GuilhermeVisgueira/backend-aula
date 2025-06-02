from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto, Cliente, Venda
from .forms import ProdutoForm, ClienteForm, VendaForm

# Listagem
def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/list.html', {'produtos': produtos})

# Criação
def cria_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'produtos/form.html', {'form': form})

# Edição
def edita_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'produtos/form.html', {'form': form})

# Remoção
def remove_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        produto.delete()
        return redirect('lista_produtos')
    return render(request, 'produtos/confirm_delete.html', {'produto': produto})

#--
def lista_clientes(request):
    form = Cliente.objects.all()
    return render(request, 'cliente_form.html', {'form': form})

def cria_cliente(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_clientes')
    return render(request, 'cliente_form.html', {'form': form})

#--

def lista_vendas(request):
    form = Venda.objects.select_related('cliente', 'produto').all()

    cliente_id = request.GET.get('cliente')
    data_inicio = request.GET.get('data_inicio')
    data_fim = request.GET.get('data_fim')

    if cliente_id:
        form = form.filter(cliente_id=cliente_id)
    if data_inicio:
        form = form.filter(data_venda__gte=data_inicio)
    if data_fim:
        form = form.filter(data_venda__lte=data_fim)

    return render(request, 'venda_form.html', {'form': form})

def cria_venda(request):
    form = VendaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_vendas')
    return render(request, 'venda_form.html', {'form': form})