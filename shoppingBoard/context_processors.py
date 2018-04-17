from cart.cart import Cart
from .models import Category

def header_nav(request):
    categories_men=Category.objects.filter(gender='Male')
    categories_women=Category.objects.filter(gender='Female')
    return {'cart': Cart(request),'categories_M':categories_men,'categories_F':categories_women}
