from django.template import Library
from utils import utils

register = Library()


@register.filter(name='format_price')
def price_formarter(val):
    return utils.price_formarter(val)
