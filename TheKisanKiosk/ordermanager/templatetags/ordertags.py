from django import template
from regex import F
from base.models import Order

register = template.Library()

@register.simple_tag
def verify(user,listing):
    orders = Order.objects.filter(buyerid__id=user).filter(listingid__id=listing)
    if orders.count() == 0:
        return False
    else:
        for order in orders:
            if order.status == 'DELIVERED':
                return True
    return False