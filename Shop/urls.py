"""Shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from shoppingBoard import views
from accounts import views as accounts_views
from cart import views as cart_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home ,name='home'),
    path('shop/<gender>/<category_name>', views.productsFromCategory, name='product_list_c'),  # url to go to category/
    path('shop/<gender>/<category_name>/<pk>', views.productDetails, name='product_details'),
    path('accounts/signup/',accounts_views.signup,name='signup'),
    path('accounts/login/',auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
   # path('logout/','django.contrib.auth.views.logout',name='logout'),
    path('ajax/add_to_cart/',cart_views.add_to_cart,name='product_to_cart'), #add a product to the cart
    path('checkout/cart',cart_views.cart_view,name='cart_view'), # cart details
    path('checkout/cart/remove/<product_id>',cart_views.cart_remove,name='remove_cart_item'),
    path('checkout/confirming',accounts_views.place_order,name='order') #remove a product from the cart
    
    #TO DO add url 
  # path('shop/<category>/<subCategory>/',views.sub_category,name='sub_category'),  #url to go to category/subCategory/*
  # path('checkout/cart',views.cart,name='cart')#url to go to cart
    #url to go to category/subCategory/*
    #url to create a account
    #url to see your account
    #url to login
    #url for checkout
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)