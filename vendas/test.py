from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Venda
from datetime import timezone


class VendasTests(TestCase):
    def test_nova_venda(self):
        response = self.client.post(
            '/vendas/nova/', {'titulo': 'Venda Teste', 'preco': '99.99'}
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Venda.objects.count(), 1)
        venda = Venda.objects.get(id=1)
        self.assertEqual(venda.titulo, 'Venda Teste')
        self.assertEqual(venda.preco, '99.99')

    def test_vendas_index(self):
        response = self.client.get('/vendas/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nenhuma venda cadastrada')

        venda = Venda.objects.create(titulo='Venda Teste', preco='99.99')
        response = self.client.get('/vendas/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Venda Teste')
        self.assertContains(response, 'R$ 99,99')


def test_delete(self):
    venda = Venda.objects.create(
        Produto='Test Produto',
        Quantidade=1,
        Vendedor='Test Vendedor',
        Pagamento='Test Pagamento',
        Preco=10.00,
        Data_criacao=timezone.now(),
    )
    response = self.client.get(reverse('delete', args=[venda.id]))
    self.assertEqual(response.status_code, 302)
    self.assertEqual(Venda.objects.count(), 0)


def test_update(self):
    venda = Venda.objects.create(
        Produto='Test Produto',
        Quantidade=1,
        Vendedor='Test Vendedor',
        Pagamento='Test Pagamento',
        Preco=10.00,
        Data_criacao=timezone.now(),
    )
    response = self.client.get(reverse('update', args=[venda.id]))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'update.html')
    response = self.client.post(
        reverse('update', args=[venda.id]),
        {
            'produto': 'Updated Test Produto',
            'quantidade': 2,
            'vendedor': 'Updated Test Vendedor',
            'pagamento': 'Updated Test Pagamento',
            'preco': 20.00,
        },
    )
    self.assertEqual(response.status_code, 302)
    venda = Venda.objects.get(id=venda.id)
    self.assertEqual(venda.Produto, 'Updated Test Produto')
    self.assertEqual(venda.Quantidade, 2)
    self.assertEqual(venda.Vendedor, 'Updated Test Vendedor')
    self.assertEqual(venda.Pagamento, 'Updated Test Pagamento')
    self.assertEqual(venda.Preco, 20.00)
