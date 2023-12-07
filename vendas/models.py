from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Venda(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    Produto = models.CharField(max_length=40)
    Quantidade = models.IntegerField(default=1)
    Preco = models.FloatField(default=0.0)
    Pagamento = models.CharField(
        max_length=30,
        choices=[
            ('Dinheiro', 'Dinheiro'),
            ('Cartão', 'Cartão'),
            ('Pix', 'Pix'),
        ],
    )
    Data_criacao = models.DateTimeField(timezone.now())
    Vendedor = models.CharField(
        max_length=30,
        choices=[
            ('Lukas', 'Lukas'),
            ('Jsantos', 'Jsantos'),
            ('Alison', 'Alison'),
            ('Edvania', 'Edvania'),
        ],
    )

    @property
    def Total(self):
        return self.Quantidade * self.Preco

    def __str__(self):
        return '{} - {} - {} - {} - {} - {} - {}'.format(
            self.Produto,
            self.Quantidade,
            self.Preco,
            'R$ {}'.format(self.Preco),
            self.Data_criacao,
            self.Vendedor,
            self.Total,
        )
