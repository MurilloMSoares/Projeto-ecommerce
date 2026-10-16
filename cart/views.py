from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import ItemCarrinho
from products.models import Produto


@login_required
def adicionar_carrinho(request, produto_id):
    if request.method != 'POST':
        return redirect('home')

    produto = get_object_or_404(Produto, id=produto_id)

    item, criado = ItemCarrinho.objects.get_or_create(
        usuario=request.user,
        produto=produto
    )

    if not criado:
        item.quantidade += 1
        item.save()

    return redirect('home')


@login_required
def ver_carrinho(request):
    itens = ItemCarrinho.objects.filter(usuario=request.user)
    total = 0

    for item in itens:
        item.subtotal = item.produto.preco * item.quantidade
        total += item.subtotal

    return render(request, 'cart/carrinho.html', {
        'itens': itens,
        'total': total
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

        elif acao == 'diminuir':
            if item.quantidade > 1:
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
    itens = ItemCarrinho.objects.filter(usuario=request.user)

    if not itens.exists():
        return redirect('carrinho')

    total = sum(
        item.produto.preco * item.quantidade
        for item in itens
    )

    return render(request, 'cart/checkout.html', {
        'itens': itens,
        'total': total
    })


@login_required
def finalizar_compra(request):
    if request.method != 'POST':
        return redirect('checkout')

    return render(request, 'cart/finalizado.html')
