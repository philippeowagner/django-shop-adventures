""" Cart modifierts for the myshop app of django-shop-adventures."""
import decimal

from django.conf import settings

from shop.cart.cart_modifiers_base import BaseCartModifier


class FixedShippingCosts(BaseCartModifier):
    """
    This will add a fixed amount of money for shipping costs.
    """
    def add_extra_cart_price_field(self, cart):
        cart.extra_price_fields.append(
            ('Shipping costs', decimal.Decimal(
                settings.SHOP_SHIPPING_FLAT_RATE)))
        return cart


class FixedTaxRate(BaseCartModifier):
    """
    This will add 19% of the subtotal of the order to the total.

    It will also take all extra price fields into consideration and add 19%
    to them as well.
    """

    def process_cart(self, cart):
        total = cart.subtotal_price
        for item in cart.extra_price_fields:
            total += item[1]
        taxes = total * decimal.Decimal('0.19')
        to_append = ('Taxes total', taxes)
        cart.extra_price_fields.append(to_append)
        return cart
