from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Venda
from datetime import datetime


def lista(request):
    if request.method == 'GET':
        vendas = Venda.objects.all().order_by('-id')
        paginator = Paginator(vendas, 10)
        page = request.GET.get('page')
        vendas = paginator.get_page(page)
        return render(request, 'lista.html', {'vendas': vendas})

    produto_filtrar = request.GET.get('produto_filtrar')
    if produto_filtrar:
        produtos = Venda.objects.filter(
            Produto__contains=produto_filtrar).order_by('-Data_criacao')
    else:
        produtos = Venda.objects.all().order_by('-Data_criacao')

    return render(request, 'lista.html', {'produtos': produtos})


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
                Data_criacao=datetime.now(),
            )
            venda.save()
            return redirect('/vendas/lista/?status=0')
        except:
            return redirect('/vendas/lista/?status=1')


def delete(request, id):
    try:
        venda = Venda.objects.get(id=id)
        venda.delete()
        return redirect('/vendas/lista/')
    except:
        return redirect('/vendas/lista/')


def update(request, id):
    venda = get_object_or_404(Venda, id=id)
    try:
        venda.Quantidade = 2
        venda.save()
        return HttpResponse('Venda atualizada com sucesso!')
    except:
        return HttpResponse('Erro ao atualizar a venda!')
