from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.FloatField()
    status = models.CharField(
        default='C',
        max_length=1,
        choices=(
            ('A', 'Aproved'),
            ('C', 'Created'),
            ('R', 'Reproved'),
            ('P', 'Processing'),
            ('S', 'Sent'),
            ('F', 'Finished'),
        )
    )

    def __str__(self):
        return f'Pedido N. {self.pk}'

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Pedidos'


class OrderItem(models.Model):
    pedido = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.CharField(max_length=255)
    product_id = models.PositiveIntegerField()
    variation = models.CharField(max_length=255)
    variation_id = models.PositiveIntegerField()
    price = models.FloatField()
    promotional_price = models.FloatField(default=0)
    amount = models.PositiveIntegerField()
    image = models.CharField(max_length=2000)

    def __str__(self):
        return f'Item do {self.order}'

    class Meta:
        verbose_name = 'Order Item'
        verbose_name_plural = 'Itens do pedido'
