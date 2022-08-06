from django.shortcuts import render,get_object_or_404,redirect
from django.views import View
from .models import Product,Category,Order,OrderItem
from .cart import Cart
from .forms import CartAddForm
from django.contrib.auth.mixins import LoginRequiredMixin

class UserHomeView(View):
    def get(self,request):
         product=Product.objects.all()
         return render(request,'shop/index.html',{'products':product})


class ProductView(View):
    def get(self,request):
        return render(request,'shop/wokshop.html')


class ProductDetailView(View):
    class_form=CartAddForm
    def get(self,request,slug):
        product=get_object_or_404(Product,slug=slug)
        return render(request,'shop/product_details.html',{'product':product,'form':self.class_form})


class CartView(View):

    def get(self,request):
        cart=Cart(request)
        total_price=cart.get_total_price()
        return render(request,'shop/cart.html',{'cart':cart,'total_price':total_price})

    def post(self,request):
        pass


class CartAddView(View):

    def post(self,request,product_id):
        cart=Cart(request)
        product=get_object_or_404(Product,id=product_id)
        form=CartAddForm(request.POST)
        if form.is_valid():
            cart.add(product,form.cleaned_data['quantity'])
        return redirect('shop:cart')


class CartRemoveView(View):
    def get(self,request,product_id):
        cart=Cart(request)
        product=get_object_or_404(Product,id=int(product_id))
        cart.remove(product)
        return redirect('shop:cart')

class OrderCreateView(LoginRequiredMixin, View):
    def get(self,request):
        cart=Cart(request)
        order=Order.objects.create(user=request.user)
        for item in cart:
            product=get_object_or_404(Product,id=int(item['id']))
            OrderItem.objects.create(order=order,product=product,quantity=item['quantity'],price=item['price'])
        cart.clear()
        return redirect('shop:order_detail',order.id)


class OrderDetailView(LoginRequiredMixin,View):
    def get(self,request,order_id):
        order=get_object_or_404(Order,id=order_id)
        return render(request,'shop/order_detail.html',{'order':order})
    def post(self):
        pass