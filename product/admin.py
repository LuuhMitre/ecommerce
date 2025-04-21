from django.contrib import admin
from product.models import Product, Variation


class VariationInLine(admin.TabularInline):
    model = Variation
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_description',
                    'get_formated_price', 'get_formated_promo_price']
    inlines = [
        VariationInLine
    ]


admin.site.register(Product, ProductAdmin)
admin.site.register(Variation)
