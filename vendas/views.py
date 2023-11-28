from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Venda
from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4


def lista(request):
    produto_filtrar = request.GET.get('produto_filtrar')

    if produto_filtrar:
        vendas = Venda.objects.filter(Produto__contains=produto_filtrar)
    else:
        vendas = Venda.objects.all()

    return render(request, 'lista.html', {'vendas': vendas})


def nova_venda(request):
    if request.method == "GET":
        status = request.GET['status']
        print(status)
        return render(request, 'lista.html')
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

        return redirect('/vendas/lista/?status=1')
    except:
        return redirect('/vendas/lista/?status=0')


def delete(request, id):
    try:
        vendas = Venda.objects.get(id=id)
        vendas.delete()
        return redirect('/vendas/lista/?status=3')
    except:
        return redirect('/vendas/lista/?status=4')


def update(request, id):
    Produto = 'produto'
    quantidade = '1'
    Venda.objects.filter(Produto=Produto).update(quantidade)
    return HttpResponse('testando')
