from django.db import models
from PIL import Image
import os
from django.conf import settings

'''
Produto:
        Produto:
            nome - Char
            descricao_curta - Text
            descricao_longa - Text
            imagem - Image
            slug - Slug
            preco_marketing - Float
            preco_marketing_promocional - Float
            tipo - Choices
                ('V', 'Variável'),
                ('S', 'Simples'),
'''


class Product(models.Model):
    name = models.CharField(max_length=255)
    short_description = models.TextField(max_length=255)
    long_description = models.TextField()
    image = models.ImageField(
        upload_to='product_images/%Y/%m/', blank=True, null=True)
    slug = models.SlugField(unique=True)
    marketing_price = models.FloatField()
    promotional_price = models.FloatField(default=0.0)
    product_type = models.CharField(
        default='V',
        max_length=1,
        choices=(
            ('V', 'Variation'),
            ('S', 'Simple'),
        ),
    )

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
        super().save(*args, **kwargs)

        max_image_size = (800)

        if self.image:
            self.resize_image(self.image, max_image_size)

    def __str__(self):
        return self.name


'''
        Variacao:
            nome - char
            produto - FK Produto
            preco - Float
            preco_promocional - Float
            estoque - Int

'''
