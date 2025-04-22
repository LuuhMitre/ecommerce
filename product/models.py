from django.db import models
from PIL import Image
import os
from django.conf import settings
from django.utils.text import slugify
from utils import utils


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Produto")
    short_description = models.TextField(
        max_length=255, verbose_name="Descrição Curta")
    long_description = models.TextField(verbose_name="Descrição")
    image = models.ImageField(
        upload_to='product_images/%Y/%m/', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    marketing_price = models.FloatField(verbose_name="Preço")
    promotional_price = models.FloatField(
        default=0.0, verbose_name="Preço Promo")
    product_type = models.CharField(
        default='V',
        max_length=1,
        choices=(
            ('V', 'Variável'),
            ('S', 'Simples'),
        ),
    )

    def get_formated_price(self):
        return utils.price_formarter(self.marketing_price)
    get_formated_price.short_description = 'Preço'

    def get_formated_promo_price(self):
        return utils.price_formarter(self.promotional_price)
    get_formated_promo_price.short_description = 'Preço Promo'

    @staticmethod
    def resize_image(img, new_width=800):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(img_full_path)
        original_width, original_height = img_pil.size
        if original_width <= new_width:
            img_pil.close()
            return

        new_height = round((new_width * original_height) / original_width)
        new_img = img_pil.resize((new_width, new_height), Image.LANCZOS)
        new_img.save(
            img_full_path,
            optimize=True,
            quality=50
        )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f'{slugify(self.name)}-{self.pk}'

        super().save(*args, **kwargs)

        max_image_size = (800)

        if self.image:
            self.resize_image(self.image, max_image_size)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Produtos'


class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True, null=True)
    price = models.FloatField()
    promotional_price = models.FloatField(default=0)
    stock = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name or self.product.name

    class Meta:
        verbose_name = 'Variation'
        verbose_name_plural = 'Variações'
