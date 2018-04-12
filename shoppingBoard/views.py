from django.shortcuts import render , HttpResponse
from .models import SubCategory , Category , Inventory
from django.http import JsonResponse

# Create your views here.
def header(request):
    categories_men=Category.objects.filter(gender='Male')
    categories_women=Category.objects.filter(gender='Female')
    return {'categories_M':categories_men,'categories_F':categories_women}
def home(request):
    categories=dict(header(request))

    return render(request,'home.html',categories)

def productsFromCategory(request,gender,category_name):
    products=dict(header(request))
    list_of_product=Inventory.objects.filter(sub_category__sub_category_name=category_name)
    products.update({'products':list_of_product})
    return render(request,'productList.html',products)

def productDetails(request,gender,category_name,pk):
    details=dict(header(request)) 
    product_info=Inventory.objects.get(pk=pk)
    details.update({'product':product_info})
    return render(request,'productDetails.html',details)
#to be send to cart application
