

CART_SESSION_ID='cart'
class Cart:
    def __init__(self,request):
        self.session=request.session
        cart=self.session.get(CART_SESSION_ID)
        if not cart:
            cart=self.session[CART_SESSION_ID]={}
        self.cart=cart

    def __iter__(self):
        cart=self.cart.copy()
        for item in cart.values():
            yield item

    def add(self,product,quantity):
        product_id=str(product.id)
        if  product_id not in self.cart:
            self.cart[product_id]={'id':str(product.id),'product':product.name,'quantity':'0','price':str(product.price),'total_price':'0'}
        quantity_value=int( self.cart[product_id]['quantity'])
        quantity_value +=quantity
        self.cart[product_id]['quantity'] =str(quantity_value)
        self.cart[product_id]['total_price'] = str(int(self.cart[product_id]['quantity']) * int(self.cart[product_id]['price']))
        self.save()

    def __len__(self):
        return sum(int(item['quantity']) for item in self.cart.values())

    def get_total_price(self):
       return sum(int(item['price']) * int(item['quantity']) for item in self.cart.values())

    def remove(self,product):
        product_id=str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        self.session.modified=True

