from django.shortcuts import render,get_object_or_404,redirect
from django.views import View
from .models import Product,Category,Order,OrderItem,Coupon
from .cart import Cart
from .forms import CartAddForm,CouponForm
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
from django.contrib import messages
import pytz


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
    form_class=CouponForm
    def get(self,request,order_id):
        order=get_object_or_404(Order,id=order_id)
        return render(request,'shop/order_detail.html',{'order':order,'form':self.form_class})
    def post(self):
        pass

class CouponPriceView(LoginRequiredMixin,View):
    form_class=CouponForm
    def post(self,request,order_id):
        form=self.form_class(request.POST)
        now=datetime.now(tz=pytz.timezone('Asia/Tehran'))
        print('here===============')
        if form.is_valid():
            cd_code=form.cleaned_data['code']
            print(cd_code)
            try:
                 coupon_validation=Coupon.objects.get(code__exact=cd_code,valid_from__lte=now,valid_to__gte=now,active=True)
                 print(coupon_validation)
            except Coupon.DoesNotExist:
                 messages.error(request,'Coupon dose not exists','error')
                 return redirect('shop:order_detail',order_id)
            order=Order.objects.get(id=order_id)
            order.discount=coupon_validation.discount
            order.save()
        return redirect('shop:final_price',order_id)

class FinalPriceView(LoginRequiredMixin,View):
    def get(self,request,order_id):
        order=Order.objects.get(id=order_id)
        return render(request,'shop/final_price.html',{'order':order})

