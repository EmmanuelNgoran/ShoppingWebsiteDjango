from decimal import Decimal
from django.conf import settings
from shoppingBoard.models import Inventory


class Cart(object):

    def __init__(self, request):
        """
        Initialize the cart.
        """
        self.session = request.session #get the current session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
       
#TO DO : change the function to support no quantity
    def __len__(self):
        """
        Count all elements in the cart.
        """
        return sum(element['quantity'] for element in self.cart.values())

    def __iter__(self):
        """
        Iterate over the elements in the cart and get the products from the database.
        """
        product_ids = self.cart.keys()
        print(product_ids)
        print(self.cart)
        #get the product objects and add them to the cart
        products = Inventory.objects.filter(id__in=product_ids)
        print(products)# for debugging  purpose
        for product in products:
            self.cart[str(product.id)]['product'] = product
        print(" the value of the product dictionnary {}".format(self.cart))
        for element in self.cart.values():
            element['price'] = Decimal(element['price'])
            element['total_price'] = element['price'] * element['quantity']
            print('cart elements are {}'.format(element))
            yield element
        # for key in self.cart.keys():
        #     yield self.cart[key]['product']

    def add(self, product, quantity=1,size='S',update_quantity=False,update_size=False):
        """
        Add a product to the cart or update its quantity.
        """
        #TO DO: modified the current function to match the database schema for the product
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 1,
                                      'price': str(product.unit_price),'size':size}
        if not update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        if update_size:
            self.cart[product_id]['size']=size
        
        self.save()

    def remove(self, product):
        """
        Remove a product from the cart.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        # update the session cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # mark the session as "modified" to make sure it is saved
        self.session.modified = True

    def clear(self):
        # empty cart
        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True

    def get_total_price(self):
        return sum(Decimal(element['price']) * element['quantity'] for element in self.cart.values())
