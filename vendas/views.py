from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Venda
from django.utils import timezone
from django.db.models import Q

from django.contrib.auth.decorators import login_required


@login_required
def lista(request):
    vendas = (
        Venda.objects.filter(cliente=request.user)
        .order_by('-Data_criacao')
        .order_by('-Data_criacao')
    )
    table_filter = request.GET.get('table_filter')
    if table_filter:
        vendas = vendas.filter(
            Q(Produto__contains=table_filter)
            | Q(Vendedor__contains=table_filter)
            | Q(Pagamento__contains=table_filter)
        ).order_by('-Data_criacao')

    paginator = Paginator(vendas, 10)
    page = request.GET.get('page')
    try:
        vendas = paginator.page(page)
    except PageNotAnInteger:
        vendas = paginator.page(1)
    except EmptyPage:
        vendas = paginator.page(paginator.num_pages)

    return render(request, 'lista.html', {'vendas': vendas})


@login_required
def nova_venda(request):
    if request.method == 'GET':
        status = request.GET.get('status')
        return render(request, 'lista.html', {'status': status})
    elif request.method == 'POST':
        produto = request.POST.get('produto')
        quantidade = request.POST.get('quantidade')
        vendedor = request.POST.get('vendedor')
        pagamento = request.POST.get('pagamento')
        preco = request.POST.get('preco')

        try:
            venda = Venda(
                Produto=produto,
                Quantidade=quantidade,
                Vendedor=vendedor,
                Pagamento=pagamento,
                Preco=preco,
                Data_criacao=timezone.now(),
            )
            venda.save()
            return redirect('/vendas/lista/?status=0')
        except:
            return redirect('/vendas/lista/?status=1')


@login_required
def delete(request, id):
    venda = get_object_or_404(Venda, id=id)
    venda.delete()
    return redirect('/vendas/lista/')


@login_required
def read(request, id):
    venda = get_object_or_404(Venda, id=id)
    return render(request, 'update.html', {'venda': venda})


@login_required
def update(request, id):
    venda = get_object_or_404(Venda, id=id)
    if request.method == 'POST':
        produto = request.POST.get('produto')
        quantidade = request.POST.get('quantidade')
        preco = request.POST.get('preco')
        pagamento = request.POST.get('pagamento')
        vendedor = request.POST.get('vendedor')

        if (
            not produto
            or not quantidade
            or not vendedor
            or not pagamento
            or not preco
        ):
            return redirect('/vendas/lista/?status=1')

        try:
            venda.Produto = produto
            venda.Quantidade = quantidade
            venda.Preco = preco
            venda.Pagamento = pagamento
            venda.Vendedor = vendedor
            venda.save()
            return redirect('/vendas/lista/?status=0')
        except:
            return redirect('/vendas/lista/?status=1')
