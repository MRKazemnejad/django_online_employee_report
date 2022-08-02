from django.shortcuts import render,get_object_or_404,redirect
from django.views import View
from .models import Product,Category
from .cart import Cart
from .forms import CartAddForm


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
        return render(request,'shop/cart.html',{'cart':cart})
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


