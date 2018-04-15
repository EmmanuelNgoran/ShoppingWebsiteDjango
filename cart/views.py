from django.shortcuts import render , HttpResponse ,  get_object_or_404 ,redirect
from shoppingBoard.models import SubCategory , Category , Inventory
from django.http import JsonResponse
from .cart import Cart 
#write try catch to catch wong data coming from the client
def add_to_cart(request):
    product_size = request.GET.get('size', None)
    product_id=request.GET.get('product_id',None)
    status=True
    cart = Cart(request) 
    product=get_object_or_404(Inventory, id=product_id)
    cart.add(product=product,size=product_size) 
    #check whether everything is correct
    if product_id==2:
        status=False
    data = {
        'ok':status,

        #Inventory.objects.filter(username__iexact=username).exists()
    }

    return JsonResponse(data)

def cart_remove(request, product_id):    
    cart = Cart(request)    
    product = get_object_or_404(Inventory, id=product_id)    
    cart.remove(product)    
    return redirect('cart:cart_detail')#to do create the cart html change


def cart_view(request):
    cart = Cart(request)   
    return render(request,'cart/view_cart.html',{'cart':cart})

# Create your views here.
