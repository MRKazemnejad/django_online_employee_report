

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
            self.cart[product_id]={'product':product.name,'quantity':0,'price':product.price,'total_price':0}
        self.cart[product_id]['quantity'] +=quantity
        self.cart[product_id]['total_price'] += str(int(self.cart[product_id]['quantity']) * int(self.cart[product_id]['price']))
        self.save()
    def get_total_price(self):
       return sum(int(item['price'] * item['quantity']) for item in self.cart.values())


    def save(self):
        self.session.modified=True

