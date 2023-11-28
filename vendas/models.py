from django.db import models


class Venda(models.Model):
    Produto = models.CharField(max_length=40)
    Quantidade = models.IntegerField()
    Preco = models.FloatField()
    Pagamento = models.CharField(
        max_length=30, choices=[('dinheiro', 'Dinheiro'), ('cartão', 'Cartão')]
    )
    Data_criacao = models.DateField()
    Vendedor = models.CharField(
        max_length=30,
        choices=[
            ('Lukas', 'Lukas'),
            ('Jsantos', 'Jsantos'),
            ('Alison', 'Alison'),
            ('Edvania', 'Edvania'),
        ],
    )
    Marca = models.CharField(max_length=30)


def __str__(self):
    return '{} - {} - {} - {} - {} - {} - {}'.format(
        self.Produto,
        self.Quantidade,
        self.Preco,
        'R$ {}'.format(self.Preco),
        self.Data_criacao,
        self.Vendedor,
        self.Marca,
    )
