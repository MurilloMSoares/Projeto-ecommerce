from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import ItemCarrinho
from products.models import Produto


@login_required
def adicionar_carrinho(request, produto_id):
    if request.method != 'POST':
        return redirect('home')

    produto = get_object_or_404(Produto, id=produto_id)

    # Se o produto já estiver no carrinho, aumenta a quantidade.
    item, criado = ItemCarrinho.objects.get_or_create(
        usuario=request.user,
        produto=produto
    )

    if not criado:
        item.quantidade += 1
        item.save()

    return redirect('home')


@login_required
def comprar_agora(request, produto_id):
    if request.method != 'POST':
        return redirect('home')

    produto = get_object_or_404(Produto, id=produto_id)

    # Guarda somente o produto escolhido para a compra direta.
    request.session['compra_direta'] = {
        'produto_id': produto.id,
        'quantidade': 1,
    }

    return redirect('checkout')


@login_required
def ver_carrinho(request):
    # Ao abrir o carrinho, deixa de usar o modo de compra direta.
    request.session.pop('compra_direta', None)

    itens = ItemCarrinho.objects.filter(usuario=request.user)
    total = 0

    for item in itens:
        item.subtotal = item.produto.preco * item.quantidade
        total += item.subtotal

    return render(request, 'cart/carrinho.html', {
        'itens': itens,
        'total': total,
    })


@login_required
def alterar_quantidade(request, item_id, acao):
    if request.method == 'POST':
        item = get_object_or_404(
            ItemCarrinho,
            id=item_id,
            usuario=request.user
        )

        if acao == 'aumentar':
            item.quantidade += 1
            item.save()

        elif acao == 'diminuir' and item.quantidade > 1:
            item.quantidade -= 1
            item.save()

    return redirect('carrinho')


@login_required
def remover_carrinho(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(
            ItemCarrinho,
            id=item_id,
            usuario=request.user
        )
        item.delete()

    return redirect('carrinho')


@login_required
def checkout(request):
    compra_direta = request.session.get('compra_direta')

    if compra_direta:
        produto = get_object_or_404(
            Produto,
            id=compra_direta['produto_id']
        )
        quantidade = max(1, int(compra_direta.get('quantidade', 1)))

        # Usa uma lista temporária, sem adicionar o produto ao carrinho.
        itens = [{
            'produto': produto,
            'quantidade': quantidade,
            'subtotal': produto.preco * quantidade,
        }]

        total = produto.preco * quantidade

    else:
        itens = ItemCarrinho.objects.filter(usuario=request.user)

        if not itens.exists():
            return redirect('carrinho')

        total = 0

        for item in itens:
            item.subtotal = item.produto.preco * item.quantidade
            total += item.subtotal

    return render(request, 'cart/checkout.html', {
        'itens': itens,
        'total': total,
        'direct_mode': bool(compra_direta),
    })


@login_required
def finalizar_compra(request):
    if request.method != 'POST':
        return redirect('checkout')

    # Esta etapa é apenas uma confirmação visual do projeto.
    request.session.pop('compra_direta', None)

    return render(request, 'cart/finalizado.html')
