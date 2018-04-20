from django.shortcuts import render , HttpResponse
from .models import SubCategory , Category , Inventory
from django.http import JsonResponse

# Create your views here.

def home(request):
    return render(request,'firstPage.html')

def productsFromCategory(request,gender,category_name):
    list_of_product=Inventory.objects.filter(sub_category__sub_category_name=category_name)
    
    return render(request,'productList.html',{'products':list_of_product})

def productDetails(request,gender,category_name,pk):
    product_info=Inventory.objects.get(pk=pk)
    return render(request,'productDetails.html',{'product':product_info})
#to be send to cart application

