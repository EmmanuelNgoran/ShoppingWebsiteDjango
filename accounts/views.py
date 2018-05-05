from django.shortcuts import render , redirect
from django.contrib.auth import login as auth_login
from .form import SignUpForm ,UserDataForm
from django.contrib.auth.models import User
from cart.cart import Cart
from shoppingBoard.models import Order , OrderItems
import datetime
import random
from django.contrib.auth.decorators import login_required


MIN_DATE=2
MAX_DATE=8
CHARGE=8
# Create your views here.
def signup(request):
    if request.method == 'POST':
        form =SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()#if the form is valid the user instance is created with form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form =SignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def place_order(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = UserDataForm(request.POST)
        user=request.user
        print(user.username)
        if form.is_valid():
            ################
            order=form.save(commit=False)
            order.user=user
            order.save()
            delivery_date=datetime.date.today()+datetime.timedelta(random.randrange(MIN_DATE,MAX_DATE,1))
            for item in cart:
                items=OrderItems.objects.create(order=order,
                product=item['product'],
                price=item['price'],
                quantity=item['quantity'],size=item['size'],
                shipping_charge=CHARGE,
                ship_date=delivery_date)
                items.save()
                
# clear the cart
            cart.clear()
        return redirect('home')
    else:
        form = UserDataForm()
    return render(request,'accounts/placeOrder.html',{'cart':cart,'form': form})

# def order_confirmed(request):

#     render(request,'something.html',{'cart':cart})