from django.shortcuts import render,get_object_or_404
from django.views import View
from .models import Product,Category


class UserHomeView(View):
    def get(self,request):
         product=Product.objects.all()
         return render(request,'shop/index.html',{'products':product})


class ProductView(View):
    def get(self,request):
        return render(request,'shop/wokshop.html')


class ProductDetailView(View):
    def get(self,request,slug):
        product=get_object_or_404(Product,slug=slug)
        return render(request,'shop/product_details.html',{'product':product})


class CartView(View):
    def get(self,request):
        return render(request,'shop/cart.html')
    def post(self,request):
        pass

